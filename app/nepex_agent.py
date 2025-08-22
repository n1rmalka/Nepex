import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
openai.api_key = os.getenv("OPENROUTER_API_KEY")

# LLM Model to use
MODEL = "meta-llama/llama-3-8b-instruct"

# Load Markdown Reference File
try:
    with open("Nepex_Agent_Guide.md", "r", encoding="utf-8") as f:
        md_context = f.read()
except FileNotFoundError:
    md_context = "No reference guide available."

def generate_output(use_case: str, user_input: str) -> str:
    """
    Generates LLM-based output based on task type and user input for QA purposes.
    """

    task_type = use_case.strip()
    user_input = user_input.strip()

    if not task_type or not user_input:
        return "⚠️ Missing task type or user input."

    # Compose user prompt
    full_prompt = f"""Act as a Senior QA Expert. Based on the task: {task_type}, use the provided format below.

User Input:
{user_input}

Please return the output in the required format only. Avoid explanations or footnotes."""

    try:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful QA assistant that creates {task_type}. Reference:\n\n{md_context}"
                },
                {
                    "role": "user",
                    "content": full_prompt
                }
            ],
            temperature=0.4,
            max_tokens=900
        )
        return response.choices[0].message["content"].strip()

    except Exception as e:
        return f"❌ Error generating response: {str(e)}"
