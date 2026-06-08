from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

def generate_answer(
    context,
    question
):

    prompt = f"""
You are a document question answering assistant.

Answer ONLY using the provided context.

DO NOT MAKE UP INFORMATION IN ANY CASE.

If the answer is not present in the context,
respond exactly:

"I could not find that information in the document."

Context:
{context}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=prompt
    )

    return response.text