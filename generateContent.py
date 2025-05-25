from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
api_key = api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
        model = "gemini-2.0-flash",
        contents =["Explain how AI works"],
        config = types.GenerateContentConfig(
            max_output_tokens = 500,
            temperature = 0.1
        )
)
print(response.text)
