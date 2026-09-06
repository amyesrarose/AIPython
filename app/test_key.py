import os
from openai import OpenAI

# Load .env file if python-dotenv is installed
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ OPENAI_API_KEY environment variable is not set!")
    exit(1)

print(f"Testing key ending in: ...{api_key[-4:]}")

try:
    client = OpenAI(api_key=api_key)
    # Ping the models endpoint to test authentication without spending credits
    models = client.models.list()
    print("✅ OpenAI API key is valid and working!")
except Exception as e:
    print("❌ API Key check failed with error:")
    print(e)