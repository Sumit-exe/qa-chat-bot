import logging
from fastapi import FastAPI, HTTPException
from app.models.schemas import AskRequest
from app.crawler.crawler import crawl_with_requests
from app.crawler.crawler_playwright import crawl_with_playwright
from app.crawler.cleaner import clean_text
from app.crawler.chunker import chunk_text
from app.embeddings.openai_embeddings import create_embedding
from app.vectorstore.chroma_store import store_chunks, search
from app.rag.qa_chain import generate_answer


logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")


app = FastAPI()


@app.post("/ask")
def ask(req: AskRequest):
    logging.info("Received new /ask request")


    # Try requests crawler first
    texts = crawl_with_requests(req.website_url)


    # Fallback to Playwright (Amazon / YouTube)
    if not texts:
        logging.info("Falling back to Playwright crawler")
        texts = crawl_with_playwright(req.website_url)

    if not texts:
        raise HTTPException(status_code=404, detail="No readable content found")


    cleaned = [clean_text(t) for t in texts]
    chunks = []
    for t in cleaned:
        chunks.extend(chunk_text(t))

    if not chunks:
        raise HTTPException(status_code=404, detail="No usable text after cleaning")


    embeddings = [create_embedding(c) for c in chunks]
    store_chunks(chunks, embeddings)


    query_embedding = create_embedding(req.question)
    results = search(query_embedding)


    retrieved_chunks = results.get("documents", [[]])[0]
    answer = generate_answer(retrieved_chunks, req.question)


    return {"answer": answer}