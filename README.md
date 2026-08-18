# AI Agent CLI

A simple, interactive CLI-based AI chat agent using OpenAI-compatible APIs. This project allows you to chat with an AI assistant directly from your terminal, track token usage, and save conversations.

---

## Features

- Interactive chat with **Markdown rendering** for better readability.
- **Token usage tracking** to monitor API consumption.
- **Save conversations** to text files for later reference.
- **Session statistics** (messages, tokens, duration).
- **Cross-platform** (Windows, Linux, macOS).
- **Minimal dependencies** for easy setup.

---

## Setup

### 1. Clone the Repository

```bash
 git clone https://github.com/Diyako-kh/Diana-agent.git
 cd Diana-agent
```

### 2. Configure API Access

- Copy the example configuration file:
```bash
  cp config.json.example config.json
```
- Edit `config.json` and add your API key, base URL, and model:
```json
  {
    "api_key": "YOUR_API_KEY",
    "base_url": "YOUR_BASE_URL",
    "model": "YOUR_MODEL"
  }
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Agent

```bash
python agent.py
```

---

## Usage

### Commands

| Command   | Description                                    |
|-----------|------------------------------------------------|
| `/exit`   | Quit the agent.                                |
| `/new`    | Start a new session.                           |
| `/clear`  | Clear the terminal and start a new session.    |
| `/save`   | Save the conversation to a text file.          |
| `/help`   | Display available commands.                    |
| `/stats`  | Show conversation statistics.                  |

### Example Session

```text
Welcome to this AI Agent.
Type /exit to quit.


Tokens: 0
You -> Hello

Diana:  
Hi! How can I help you today?                                                                                                                                           

Tokens: 97
You -> What can you do?

Diana:  
I can help with a lot of things, like:                                                                                                                                  

 • Answering questions and explaining concepts                                                                                                                          
 • Writing, editing, and brainstorming                                                                                                                                  
 • Helping with coding or technical problems                                                                                                                            
 • Planning, organizing, and summarizing info                                                                                                                           
 • Giving recommendations or walking through decisions                                                                                                                  

Basically, if it involves thinking, writing, or figuring something out, just ask.                                                                                       

Tokens: 337
You -> 
```

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contributing

Contributions are welcome! Open an issue or submit a pull request.

---

## Acknowledgments

- [OpenAI](https://openai.com) for the API.
- [Rich](https://github.com/Textualize/rich) for Markdown rendering.
- [Colorama](https://github.com/tartley/colorama) for cross-platform colors.
