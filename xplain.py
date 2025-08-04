import sys
import os
from dotenv import load_dotenv
from rich.markdown import Markdown
from rich.console import Console
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
        {"role": "system", "content": "You explain Unix commands in beginner-friendly language, and provide clear, useful examples showing how the command is typically used. KEEP IT SUPER SHORT AND IN A SMALL FORMAT! ALSO, REMEMBER THAT YOU ARE A CLI-TOOL. YOU GIVE OUTPUTS IN TERMINALS. AVOID .MD FORMAT!"},
        {"role": "user", "content": f"Explain the command `{userCommand}`"}
    ],
    temperature=0.2
)

console = Console()
markdown = Markdown(completion.choices[0].message.content.strip())
console.print(markdown)