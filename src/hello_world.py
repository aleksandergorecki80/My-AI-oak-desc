
from utils.groq_setup import init_groq_client

client, groq_model = init_groq_client()

# Create a simple "Hello, world!" message
question = "Say any silly name and tell me what 2+2 equals."

messages = [{"role": "user", "content": question}]

print("\n📤 Sending request to Groq API...")

# Make API call
response = client.chat.completions.create(
    model=groq_model,
    messages=messages
)

# Print the response
print(f"Question: {question}")

print("\n📥 Response received:")
print("=" * 50)
print(response.choices[0].message.content)
print("=" * 50)
print("\n✓ Successfully connected to Groq model!")

# Create a more complex message

question = "What is a good investment for the next 10 years?"
messages = [{"role": "user", "content": question}]

# Make API call
response = client.chat.completions.create(
    model=groq_model,
    messages=messages
)

# Print the response
print(f"Question: {question}")
print("\n📥 Response received:")
print("=" * 50)
print(response.choices[0].message.content)
print("=" * 50)
print("\n✓ Successfully connected to Groq model!")