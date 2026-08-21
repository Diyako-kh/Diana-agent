import json
import datetime
import getpass
import sys
import random
import string
from openai import OpenAI
import os
from sys import platform
from colorama import Fore, init, Style
from rich.console import Console
from rich.markdown import Markdown


init()
console = Console()
token_tracking = 0 
start_time = datetime.datetime.now()
texts = []
session_id = f"diana_{datetime.datetime.now().strftime('%Y%m%d')}_{''.join(random.choice(string.ascii_lowercase) + random.choice(string.digits) for _ in range(6))}"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SYSTEM_PROMPT = (
    "Your name is Diana. Be helpful, concise, and natural. "
    "Never state your name in every response — only mention it if asked directly."
)


def save_session():
    if len(conv_history) > 1:
        os.makedirs(os.path.join(BASE_DIR, "sessions"), exist_ok=True)
        with open(f"{os.path.join(BASE_DIR, 'sessions', session_id)}.json", 'w', encoding='utf-8') as f:
            session = {
                    'session_id': session_id,
                    'created_at': datetime.datetime.now().strftime("%Y%m%d_%H%M%S"),
                    'model': config['model'],
                    'messages': conv_history,
                    'tokens': token_tracking
                    }
            json.dump(session, f)


try:
    with open(os.path.join(BASE_DIR, 'config.json'), 'r', encoding='utf-8') as f:
        config = json.load(f)

except FileNotFoundError:
    with open(os.path.join(BASE_DIR, 'config.json'), 'w', encoding='utf-8') as f:
        base_url = input("Enter Provider Base URL: ")
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

conv_history = [{"role": "system", "content" : SYSTEM_PROMPT}]

print("Welcome to this AI Agent.")
print("Type /exit to quit.\n")

while True:
    try:
        print(f"\nTokens: {token_tracking} | {session_id} | {config['model']}")
        text = input(Fore.CYAN + "You -> " + Style.RESET_ALL)

    except KeyboardInterrupt:
        save_session()
        print("\nGoodbye")
        sys.exit()

    if text == "/exit":
        save_session()
        print("\nGoodbye")
        break

    elif text == "/clear":
        save_session()
        conv_history = [{"role": "system", "content" : SYSTEM_PROMPT}]
        print("\nConversation Cleared")

        token_tracking = 0
        start_time = datetime.datetime.now()
        session_id = f"diana_{datetime.datetime.now().strftime('%Y%m%d')}_{''.join(random.choice(string.ascii_lowercase) + random.choice(string.digits) for _ in range(6))}"

        if platform == "win32":
            os.system("cls")

        else:
            os.system("clear")

        continue

    elif text == "/new":
        save_session()
        conv_history = [{"role": "system", "content" : SYSTEM_PROMPT}]
        print("\nNew Session Started")

        token_tracking = 0
        start_time = datetime.datetime.now()
        session_id = f"diana_{datetime.datetime.now().strftime('%Y%m%d')}_{''.join(random.choice(string.ascii_lowercase) + random.choice(string.digits) for _ in range(6))}"

        continue

    elif text == "/save":
        conversation_file = f"chat_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        os.makedirs(os.path.join(BASE_DIR, 'chats'), exist_ok=True)
        with open(os.path.join(BASE_DIR, 'chats', conversation_file), "w", encoding='utf-8') as f:
            for msg in conv_history:
                if msg['role'] != 'system':
                    f.write(f"{'Diana' if msg['role'] == 'assistant' else 'You'} : {msg['content']}\n")
            f.write(f"\n\nTotal Tokens Used: {token_tracking}\n")
            f.write(f"The Model Used: {config['model']}\n")
            f.write(f"Session Length: {int((datetime.datetime.now() - start_time).total_seconds() // 60)} min\n")
            f.write(f"Session ID: {session_id}\n")

        print(f"Conversation saved in : {conversation_file}")
        continue

    elif text == "/sessions":
        try:
            sessions = os.listdir(os.path.join(BASE_DIR, "sessions"))
            counter = 1
            session_files = []
            for session in sessions:
                if session.startswith('diana_'):
                    session_files.append(session)
                    print(f"{counter} - {session[:-5]}")
                    counter += 1

            if session_files == []:
                print("No saved sessions yet.")
                continue

            session_choose = input("Enter a Session or 0 to continue: ")
            if session_choose == '0':
                continue

            elif session_choose.isdigit() and int(session_choose) <= len(session_files):
                with open(os.path.join(BASE_DIR, 'sessions', session_files[int(session_choose) - 1])) as f:
                    session_load = json.load(f)
                    print(f"\n{'-' * 10} Messages {'-' * 10}\n")
                    for msg in session_load['messages']:
                        if msg['role'] != 'system':
                            print(f"{'Diana' if msg['role'] == 'assistant' else 'You'} : {msg['content']}\n") # use rich.Markdown to print
                    save_session()
                    session_id = session_load['session_id']
                    conv_history = session_load['messages']
                    token_tracking = session_load['tokens']
                    start_time = datetime.datetime.now()

                continue

            else:
                for session in session_files:
                    if session_choose == session[:-5]:
                        with open(os.path.join(BASE_DIR, 'sessions', session)) as f:
                            session_load = json.load(f)
                            print(f"\n{'-' * 10} Messages {'-' * 10}\n")
                            for msg in session_load['messages']:
                                if msg['role'] != 'system':
                                    print(f"{'Diana' if msg['role'] == 'assistant' else 'You'} : {msg['content']}\n") # use rich.Markdown to print
                            save_session()
                            session_id = session_load['session_id']
                            conv_history = session_load['messages']
                            token_tracking = session_load['tokens']
                            start_time = datetime.datetime.now()

                continue

        except Exception as e:
            print(f"Error: {e}")
            continue



    elif text == "/help":
        help_text = "\n**Available Commands:**\n- `/exit` - Exit the program\n- `/new` - To start a new session\n- `/clear` - Starts a new session and clear the terminal\n- `/save` - Save the current conversation to a text file\n- `/stats` - Show conversation statistics\n- `/help` - Show the available commands\n"
        console.print(Markdown(help_text))
        continue

    elif text == '/stats':
        usr_mgs = sum(1 for i in conv_history if i["role"] == 'user')
        assistant_msg = sum(1 for i in conv_history if i["role"] == 'assistant')

        stats = f"\n\n**Conversation Stats:**\n- Total Messages: {usr_mgs + assistant_msg}\n- User Messages: {usr_mgs}\n- Assistant Messages: {assistant_msg}\n- Total Token Used: {token_tracking}\n- Session Length: {int((datetime.datetime.now() - start_time).total_seconds() // 60)} min"
        console.print(Markdown(stats))
        continue

    elif not text.strip():
        continue

    conv_history.append({"role": "user", "content": text})

    if len(conv_history) > 21:
        texts =  [conv_history[0]] + conv_history[-20:]
    else:
        texts = conv_history.copy()


    try:
        response = client.chat.completions.create(
            model=config['model'],
            messages=texts,
            temperature=0.2
        )
        
        if response.usage:
            token_tracking += response.usage.total_tokens or 0

        assistant_reply = response.choices[0].message.content
        
        conv_history.append({"role": "assistant", "content": assistant_reply})


        print(f"\n{Fore.YELLOW}Diana:  {Style.RESET_ALL}")
        console.print(Markdown(assistant_reply))

    except Exception as e:
        print(f"Something went wrong: {e}")
        if conv_history[-1]['role'] == 'user':
            conv_history.pop()

        continue
