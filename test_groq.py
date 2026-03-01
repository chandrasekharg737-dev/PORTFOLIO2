from groq import Groq
import os

# Use the key provided by the user
api_key = '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'

try:
    print("Initializing Groq client...")
    client = Groq(api_key=api_key)

    print("Sending test request...")
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, are you working?"}
        ],
        temperature=0.7,
        max_tokens=50,
        top_p=1,
        stream=False,
        stop=None,
    )

    print("Response received:")
    print(completion.choices[0].message.content)
    print("\nAPI Test PASSED.")

except Exception as e:
    print(f"\nAPI Test FAILED. Error: {e}")
