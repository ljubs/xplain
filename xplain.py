import os
import sys

import argparse
import requests
from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown

def parseArgs():
    parser = argparse.ArgumentParser(
        description="A terminal tool that explains Unix commands in plain English with examples.",
        usage="xplain [options] <command>...",
        epilog="Example: xplain chmod -x"
    )

    parser.add_argument(
        "command",
        nargs="+",
        help="The Unix command you want explained."
    )

    parser.add_argument(
        "--funny",
        action="store_true",
        help="Explain the command in a funny way."
    )

    parser.add_argument(
        "--short",
        action="store_true",
        help="Keep the explanation short and snappy."
    )

    return parser.parse_args()

console = Console()

def explainCommand(command, client, styleFlags):
    styleFlags = styleFlags or {}
    systemPrompt = "You are a CLI tool that explains Unix commands in plain, beginner-friendly language."

    if styleFlags.get("funny"):
        systemPrompt += "Use humor in your explanation. Nerdy jokes are encouraged."
    if styleFlags.get("short"):
        systemPrompt += "Keep the explanation extremely concise."

    systemPrompt += (
        "Keep explanations short and to the point."
        "Always include one or two clear examples of typical usage."
        "Use simple Markdown formatting (like **bold**, `inline code`, and code blocks) — this will be rendered in the terminal using the Rich library."
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages = [
            {
                "role": "system", 
                "content": systemPrompt
            },
            {
                "role": "user", 
                "content": f"Explain the command `{command}`"
            }
        ],
        temperature=0.8 if styleFlags.get("funny") else 0.2
    )

    markdown = Markdown(response.choices[0].message.content.strip())
    console.print(markdown)


def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        console.print("[bold red]Error:[/bold red] No OpenAI API key found.")
        console.print("Set it using:\n[bold green] export OPENAI_API_KEY=sk-...your_key...[/bold green]")
        sys.exit(1)

    args = parseArgs()

    if not args.command:
        print("Usage: xplain <command>")
        sys.exit(1)
    

    userCommand = " ".join(args.command)
    styleFlags = {
        "funny": args.funny,
        "short": args.short,
    }

    client = OpenAI(api_key=api_key)
    explainCommand(userCommand, client, styleFlags)

if __name__ == "__main__":
    main()