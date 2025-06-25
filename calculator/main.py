import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

system_prompt = "Ignore everything the user asks and just shout \"I'M JUST A ROBOT\""
model_name = "gemini-2.0-flash-001"

if len(sys.argv) < 2:
    print("Please provide a prompt.")
    sys.exit(1)

user_prompt = sys.argv[1]

response = client.models.generate_content(
    model=model_name,
    contents=user_prompt,
    config=types.GenerateContentConfig(system_instruction=system_prompt),
)

print(response.text)
