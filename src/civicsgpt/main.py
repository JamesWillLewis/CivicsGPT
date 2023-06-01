import os
import sys

import openai

GPT_MODEL = "gpt-3.5-turbo"
MAX_TOKENS_DEFAULT = 16
TEMPERATURE_DEFAULT = 0.2
DEFAULT_PROMPT = "I forgot to ask something."

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PROMPT

completion_args = {}
if len(sys.argv) > 2:
    completion_args['temperature'] = float(sys.argv[2])
if len(sys.argv) > 3:
    completion_args['max_tokens'] = int(sys.argv[3])

print(f"You asked: '{prompt}' with args: {completion_args}")
print(f'Using model {GPT_MODEL}')

response = openai.ChatCompletion.create(
    model=GPT_MODEL,
    messages=[
        {"role": "user", "content": prompt},
    ],
    **completion_args)
print(f'GPT says: {response}')
