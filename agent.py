import json
import datetime
import getpass
import sys
from openai import OpenAI
from os import system
from sys import platform
from colorama import Fore, init, Style
from rich.console import Console
from rich.markdown import Markdown


init()
console = Console()
token_tracking = 0 
start_time = datetime.datetime.now()

try:
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)

except FileNotFoundError:
    with open('config.json', 'w') as f:
        base_url = input("Enter Porvider Base URL: ")
        api_key = getpass.getpass("Enter API Key: ")
        model = input("Enter Model: ")

        config = {
                'api_key': api_key,
                'base_url': base_url,
                'model': model
                }
        json.dump(config, f)

except json.JSONDecodeError:
    print("config.json is invalid.")
    sys.exit()

except Exception as e:
    print(f"Something went wrong {e}")
    sys.exit()


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
        sys.exit()

    if text == "/exit":
        print("\nGoodbye")
        break

    elif text == "/clear":
        texts = [{"role": "system", "content" : "Your name is Diana. Be helpful, concise, and natural. Never state your name in every response — only mention it if asked directly."}]
        print("\nConversation Cleared")

        token_tracking = 0
        start_time = datetime.datetime.now()

        if platform == "win32":
            system("cls")

        else:
            system("clear")

        continue

    elif text == "/new":
        texts = [{"role": "system", "content" : "Your name is Diana. Be helpful, concise, and natural. Never state your name in every response — only mention it if asked directly."}]
        print("\nNew Session Started")

        token_tracking = 0
        start_time = datetime.datetime.now()

        continue

    elif text == "/save":
        conversation_file = f"chat_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(conversation_file, "w", encoding='utf-8') as f:
            for msg in texts:
                if msg['role'] != 'system':
                    f.write(f"{'Diana' if msg['role'] == 'assistant' else 'You'} : {msg['content']}\n")
            f.write(f"\n\nTotal Tokens Used: {token_tracking}\n")
            f.write(f"The Model Used: {config['model']}\n")
            f.write(f"Session Length: {(datetime.datetime.now() - start_time).total_seconds() // 60} min\n")

        print(f"Conversation saved in : {conversation_file}")
        continue

    elif text == "/help":
        help_text = "\n**Available Commands:**\n- `/exit` - Exit the program\n- `/new` - To start a new session\n- `/clear` - Starts a new session and clear the terminal\n- `/save` - Save the current conversation to a text file\n- `/stats` - Show conversation statistics\n- `/help` - Show the available commands\n"
        console.print(Markdown(help_text))
        continue

    elif text == '/stats':
        usr_mgs = sum(1 for i in texts if i["role"] == 'user')
        assistant_msg = sum(1 for i in texts if i["role"] == 'assistant')

        stats = f"\n\n**Conversation Stats:**\n- Total Messages: {usr_mgs + assistant_msg}\n- User Messages: {usr_mgs}\n- Assistant Messages: {assistant_msg}\n- Total Token Used: {token_tracking}\n- Session Length: {(datetime.datetime.now() - start_time).total_seconds() // 60} min"
        console.print(Markdown(stats))
        continue

    elif not text.strip():
        continue

    texts.append({"role": "user", "content": text})
    
    try:
        response = client.chat.completions.create(
            model=config['model'],
            messages=texts,
            temperature=0.2
        )
        
        if response.usage:
            token_tracking += response.usage.total_tokens

        assistant_reply = response.choices[0].message.content
        
        texts.append({"role": "assistant", "content": assistant_reply})

        if len(texts) > 21:
            texts =  [texts[0]] + texts[-20:]


        print(f"\n{Fore.YELLOW}Diana:  {Style.RESET_ALL}")
        console.print(Markdown(assistant_reply))

    except Exception as e:
        print(f"Something went wrong: {e}")
        if texts[-1]['role'] == 'user':
            texts.pop()

        continue
