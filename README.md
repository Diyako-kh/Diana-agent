# Diana Agent

A simple, interactive CLI-based AI chat agent using OpenAI-compatible APIs. This project allows you to chat with an AI assistant directly from your terminal, track token usage, and save conversations.

---

## Features

- Interactive chat with **Markdown rendering** for better readability.
- **Token usage tracking** to monitor API consumption.
- **Save conversations** to text files for later reference.
- **Session statistics** (messages, tokens, duration).
- **Session tracking** (save/load sessions with `/sessions`).
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

| Command     | Description                                    |
|------------|------------------------------------------------|
| `/exit`     | Quit the agent.                                |
| `/new`      | Start a new session.                           |
| `/clear`    | Clear the terminal and start a new session.    |
| `/save`     | Save the conversation to a text file.          |
| `/help`     | Display available commands.                    |
| `/stats`    | Show conversation statistics.                  |
| `/sessions` | List and load previous sessions.               |

### Example Session

```text
Welcome to this AI Agent.
Type /exit to quit.


Tokens: 0 | diana_20260819_o4e6y2k7i4r3 | tencent-hy3-free
You -> Hello there 

Diana:  
Hi! How can I help you today?                                                                                                                                          

Tokens: 105 | diana_20260819_o4e6y2k7i4r3 | tencent-hy3-free
You -> What can you do?         

Diana:  
I can help with a wide range of things, like:                                                                                                                          

 • Answering questions and explaining concepts                                                                                                                         
 • Writing, editing, or brainstorming content                                                                                                                          
 • Summarizing text or articles                                                                                                                                        
 • Helping with code or technical problems                                                                                                                             
 • Planning, organizing, or decision-making                                                                                                                            
 • Casual conversation or recommendations                                                                                                                              

What do you need a hand with?                                                                                                                                          

Tokens: 337 | diana_20260819_o4e6y2k7i4r3 | tencent-hy3-free
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
