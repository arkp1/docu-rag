from google import genai
import os


client = genai.Client(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

def rewrite_query(question):
   
    prompt = f"""
    You are a retrieval query optimizer.

    Rewrite the user's question into a concise query
    for semantic document retrieval.

    Rules:
    - Preserve all names, places, and entities exactly as written.
    - Do NOT correct spelling.
    - Do NOT add facts.
    - Do NOT infer locations.
    - Do NOT infer people.
    - Do NOT answer the question.
    - Keep important keywords.
    - Translate non-English queries to English.
    - Return only the rewritten query.

    Question:
    {question}
    """

    response = (
            client.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=prompt
            )
        )

    return response.text.strip()
