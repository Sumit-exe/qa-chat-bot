def chunk_text(text, size=400, overlap=80):
    words = text.split()
    chunks = []

    for i in range(0, len(words), size - overlap):
        chunks.append(" ".join(words[i:i + size]))

    return chunks