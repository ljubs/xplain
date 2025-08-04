import sys
import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if len(sys.argv) < 2:
    print("Usage: xplain <command>")
    exit(1)

userCommand = " ".join(sys.argv[1:])

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages = [
        {"role": "system", "content": "You explain Unix commands in beginner-friendly language, and provide clear, useful examples showing how the command is typically used."},
        {"role": "user", "content": f"Explain the command `{userCommand}`"}
    ],
    temperature=0.2
)

print(completion.choices[0].message)
