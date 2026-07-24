# Simple AI Chatbot

A beginner-friendly AI chatbot built with Python.

## Features
- Simple conversation system
- Easy to understand code
- Works with OpenAI / Grok / Claude API

## How to use
1. Install library: `pip install openai`
2. Create a file named `chatbot.py`
3. Paste the code (given below)
4. Add your API key and run

## chatbot.py Code

from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY_HERE")

def chat(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

print("Simple AI Chatbot started! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        print("AI: Goodbye!")
        break
    reply = chat(user_input)
    print("AI:", reply)
