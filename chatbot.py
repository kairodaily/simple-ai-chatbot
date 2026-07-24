from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY_HERE")

def chat(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

print("AI Chatbot started! Type exit to quit")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("AI: Goodbye!")
        break
    print("AI:", chat(user))
