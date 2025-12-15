import hashlib
from openai import OpenAI
from app.config import OPENAI_API_KEY, EMBEDDING_MODEL


client = OpenAI(api_key=OPENAI_API_KEY)

_embedding_cache = {}

def _hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

def create_embedding(text: str):
    key = _hash(text)

    if key in _embedding_cache:
        return _embedding_cache[key]

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )

    embedding = response.data[0].embedding
    _embedding_cache[key] = embedding
    return embedding