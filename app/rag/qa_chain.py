from openai import OpenAI
from app.config import OPENAI_API_KEY, CHAT_MODEL


client = OpenAI(api_key=OPENAI_API_KEY)

def generate_answer(chunks, question):
    if not chunks:
        return "Information not found on this website."

    context = "\n".join(chunks)

    prompt = f"""
    Answer ONLY from the context below.
    If not present, say: Information not found on this website.

    Context:
    {context}

    Question:
    {question}
    """

    resp = client.chat.completions.create(
    model=CHAT_MODEL,
    messages=[{"role": "user", "content": prompt}],
    temperature=0
    )

    return resp.choices[0].message.content