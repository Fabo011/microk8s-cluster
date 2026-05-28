import os
import pandas as pd
import requests

# Paths
INPUT_FILE = "files/bronze-raw/mall_customers.csv"
OUTPUT_DIR = "files/silver/"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "mall_customers_silver.csv")
PROMPT_FILE = "prompt-templates/bronze-to-silver-prompt.md"

# LM Studio config (OpenAI-compatible API)
#LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
LM_STUDIO_URL = "http://host.docker.internal:1234/v1/chat/completions"
MODEL_NAME = "qwen3.5-9b"

def load_prompt():
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        return f.read()

def load_csv_as_string():
    df = pd.read_csv(INPUT_FILE)
    return df.to_csv(index=False)

def build_prompt(template: str, csv_data: str):
    return template.replace("{{input_csv}}", csv_data)

def call_llm(prompt: str):
    payload = {
    "model": MODEL_NAME,
    "messages": [
        {
            "role": "system",
            "content": "You are a strict CSV transformation engine. Output ONLY final CSV. No reasoning."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    "temperature": 0.0,
    "max_tokens": 500
     }

    response = requests.post(LM_STUDIO_URL, json=payload)
    response.raise_for_status()

    msg = response.json()["choices"][0]["message"]

    return msg.get("content") or msg.get("reasoning_content")

def save_output(csv_text: str):
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(csv_text.strip() + "\n")

def main():
    print("Loading prompt...")
    template = load_prompt()

    print("Loading CSV...")
    csv_data = load_csv_as_string()

    print("Building prompt...")
    prompt = build_prompt(template, csv_data)

    print("Calling LM Studio...")
    result = call_llm(prompt)

    print("Saving output...")
    save_output(result)

    print(f"Done → {OUTPUT_FILE}")

if __name__ == "__main__":
    main()