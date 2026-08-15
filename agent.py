import json
from openai import OpenAI

with open('config.json', 'r') as f:
    config = json.load(f)

client = OpenAI(
    api_key=config['api_key'],
    base_url=config['base_url']
)

texts = [    {"role": "system", "content" : "Your name is Diana, and you are a helpful AI assistant."}]

print("Welcome to this AI Agent.")
print("Type /exit to quit.")
while True:
    text = input("\nYou -> ")

    if text == "/exit":
        print("Goodbye")
        break
    
    texts.append({"role": "user", "content": text})

    response = client.chat.completions.create(
        model=config['model'],
        messages=texts,
        temperature=0.2
    )

    assistant_reply = response.choices[0].message.content.replace('\n', '', 2)

    texts.append({"role": "assistant", "content": assistant_reply})

    print(f"\nDiana -> {assistant_reply}")
