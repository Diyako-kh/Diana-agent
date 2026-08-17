import json
import datetime
import getpass
from openai import OpenAI
from os import system
from sys import platform
from colorama import Fore, init, Style
from rich.console import Console
from rich.markdown import Markdown


init()
console = Console()
token_tracking = 0 

try:
    with open('config.json', 'r') as f:
        config = json.load(f)
except FileNotFoundError:
    with open('config.json', 'w') as f:
        base_url = input("Enter your porviders base url: ")
        api_key = getpass.getpass("Enter your api key: ")
        model = input("Enter the model you want to use: ")

        config = {
                'api_key': api_key,
                'base_url': base_url,
                'model': model
                }
        json.dump(config, f)
except Exception as e:
    print(f"Something went wrong {e}")
    exit()

client = OpenAI(
    api_key=config['api_key'],
    base_url=config['base_url']
)

texts = [{"role": "system", "content" : "Your name is Diana. Be helpful, concise, and natural. Never state your name in every response — only mention it if asked directly."}]

print("Welcome to this AI Agent.")
print("Type /exit to quit.\n")

while True:
    try:
        print(f"\nTokens: {token_tracking} | Session: Not developed yet.")
        text = input(Fore.CYAN + "You -> " + Style.RESET_ALL)

    except KeyboardInterrupt:
        print("\nGoodbye")
        exit()

    if text == "/exit":
        print("Goodbye")
        break

    elif text == "/new":
        texts = [{"role": "system", "content" : "Your name is Diana. Be helpful, concise, and natural. Never state your name in every response — only mention it if asked directly."}]
        print("\nConversation cleared")
        token_tracking = 0
        if platform == "win32":
            system("cls")
        else:
            system("clear")
        continue

    elif text == "/save":
        conversation_file = f"chat_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(conversation_file, "w") as f:
            for msg in texts:
                if msg['role'] != 'system':
                    f.write(f"{msg['role']} : {msg['content']}\n")

        print(f"Conversation saved in : {conversation_file}")
        continue

    elif text == "/help":
        pass # Code it later.

    elif not text.strip():
        continue

    texts.append({"role": "user", "content": text})
    
    try:
        response = client.chat.completions.create(
            model=config['model'],
            messages=texts,
            temperature=0.2
        )
        
        token_tracking += response.usage.total_tokens

        assistant_reply = response.choices[0].message.content
        
        if len(texts) > 21:
            texts =  [texts[0]] + texts[-20:]

        texts.append({"role": "assistant", "content": assistant_reply})
        
        print(f"\n{Fore.YELLOW}Diana:  {Style.RESET_ALL}")
        console.print(Markdown(assistant_reply))

    except Exception as e:
        print(f"Something went wrong: {e}")
        continue
