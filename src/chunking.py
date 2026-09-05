def chunk_text(text, max_chars=1500):
    """
    Split long text into semantic chunks.
    """

    words = text.split()

    chunks = []
    current_chunk = []

    current_length = 0

    for word in words:

        if current_length + len(word) + 1 > max_chars:
            chunks.append(" ".join(current_chunk))
            current_chunk = [word]
            current_length = len(word)

        else:
            current_chunk.append(word)
            current_length += len(word) + 1

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks


if __name__ == "__main__":

    sample_text = "AI " * 3000

    chunks = chunk_text(sample_text)

    print(f"Total chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks):
        print(f"Chunk {i+1}: {len(chunk)} characters")
