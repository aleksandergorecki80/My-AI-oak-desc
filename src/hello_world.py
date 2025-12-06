
# Load environment variables
from dotenv import load_dotenv
import os
from pathlib import Path

# Get project root directory (parent of __my_scripts__)
project_root = Path(__file__).parent.parent

# Load .env file from project root
env_path = project_root / '.env'
load_dotenv(dotenv_path=env_path, override=True)

# Import Groq
from groq import Groq

# Get API key from environment
groq_api_key = os.getenv('GROQ_API_KEY')
groq_model = os.getenv('GROQ_MODEL')

if not groq_api_key:
    print("Error: GROQ_API_KEY not found in environment variables!")
    print("Please add GROQ_API_KEY to your .env file in the project root.")
    exit(1)

print(f"✓ Groq API Key found (begins with: {groq_api_key[:8]})")

# Create Groq client
client = Groq(api_key=groq_api_key)
print("✓ Groq client created successfully")

# Create a simple "Hello, world!" message
messages = [{"role": "user", "content": "Say any silly name and tell me what 2+2 equals."}]

print("\n📤 Sending request to Groq API...")

# Make API call
response = client.chat.completions.create(
    model=groq_model,
    messages=messages
)

# Print the response
print("\n📥 Response received:")
print("=" * 50)
print(response.choices[0].message.content)
print("=" * 50)
print("\n✓ Successfully connected to Groq model!")

