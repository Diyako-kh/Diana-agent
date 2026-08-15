import json
from openai import OpenAI

with open('config.json', 'r') as f:
    config = json.load(f)

client = OpenAI(
    api_key=config['api_key'],
    base_url=config['base_url']
)

response = client.chat.completions.create(
    model=config['model'],
    messages=[{"role": "user", "content": "Hello, What's up?"}]
)

print(response.choices[0].message.content)
