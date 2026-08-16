import json
import datetime
from os import system
from openai import OpenAI
from colorama import Fore, init, Style


init()

with open('config.json', 'r') as f:
    config = json.load(f)

client = OpenAI(
    api_key=config['api_key'],
    base_url=config['base_url']
)

texts = [{"role": "system", "content" : "Your name is Diana."}]

print("Welcome to this AI Agent.")
print("Type /exit to quit.\n")
print("Token used: 0")

while True:
    try:
        text = input(Fore.CYAN + "You -> " + Style.RESET_ALL)

    except KeyboardInterrupt:
        print("\nGoodbye")
        exit()

    if text == "/exit":
        print("Goodbye")
        break

    elif text == "/new":
        texts = [{"role": "system", "content" : "Your name is Diana."}]
        print("\nConversation cleared")
        continue
    elif text == "/save":
        conversation_file = f"chat_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(conversation_file, "w") as f:
            for msg in texts:
                if msg['role'] != 'system':
                    f.write(f"{msg['role']} : {msg['content']}\n")

        print(f"Conversation saved in : {conversation_file}")
        continue

    texts.append({"role": "user", "content": text})
    
    try:
        response = client.chat.completions.create(
            model=config['model'],
            messages=texts,
            temperature=0.2
        )

        assistant_reply = response.choices[0].message.content.replace('\n', '', 2)
        
        if len(text) > 21:
            texts =  [texts[0]] + texts[-20:]

        texts.append({"role": "assistant", "content": assistant_reply})

        print(Fore.YELLOW + f"\nDiana -> {Style.RESET_ALL + assistant_reply}")
        print(f"\nToken used: {response.usage.total_tokens}")

    except Exception as e:
        print(f"Something went wrong: {e}")
        break
