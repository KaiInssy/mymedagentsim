import os
import requests
import json

API_BASE = "https://api.deepseek.com/v1"
API_KEY = os.environ.get("DEEPSEEK_API_KEY")

if not API_KEY:
  raise SystemExit("Set DEEPSEEK_API_KEY environment variable first")

headers = {
  "Authorization": f"Bearer {API_KEY}",
  "Content-Type": "application/json"
}

payload = {
  "model": "deepseek-chat",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello"}
  ],
  "stream": False
}

resp = requests.post(f"{API_BASE}/chat/completions", headers=headers, data=json.dumps(payload), timeout=30)
resp.raise_for_status()
data = resp.json()
print(data["choices"][0]["message"]["content"])