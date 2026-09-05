import json
from chunking import chunk_text
#----------------------------
# Mock LLM Providers
# -----------------------------

def gemini_extract(text):
    print("Trying Gemini Flash...")

    if len(text) < 20:
        raise Exception("Gemini Failed")

    return {
        "provider": "Gemini Flash",
        "summary": text[:100]
    }


def groq_extract(text):
    print("Trying Groq Llama3...")

    return {
        "provider": "Groq Llama3",
        "summary": text[:100]
    }


def deepseek_extract(text):
    print("Trying DeepSeek...")

    return {
        "provider": "DeepSeek",
        "summary": text[:100]
    }


# -----------------------------
# Fallback Engine
# -----------------------------

def extract_with_fallback(text):

    providers = [
        gemini_extract,
        groq_extract,
        deepseek_extract
    ]

    for provider in providers:
        try:
            result = provider(text)
            print(f"Success using {result['provider']}")
            return result

        except Exception as e:
            print("Provider failed:", e)

    raise Exception("All providers failed.")


# -----------------------------
# Test
# -----------------------------

if __name__ == "__main__":


    sample_text = """
         OpenAI released a new reasoning model today.
         The model improves coding and mathematical reasoning.
         Researchers also published benchmarks on Arxiv.
         """

    chunks = chunk_text(sample_text)

print(f"Processing {len(chunks)} chunks...")

results = []

for chunk in chunks:
    results.append(extract_with_fallback(chunk))

print(json.dumps(results[0], indent=4))