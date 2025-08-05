# xplain

Ever stared at a man page and thought, “There’s got to be a simpler way to explain this”? That’s where `xplain` comes in. It’s a CLI tool that explains Unix commands in plain English, with real examples you can actually understand. Whether you’re just getting started or you’ve been around the terminal block, `xplain` makes command-line help faster, clearer, and even a little fun, powered by a LLM via the OpenAI API.

![xplain demo](image.png)

## Installation
```bash
git clone https://github.com/yourusername/xplain.git
cd xplain
pip install .
```

## Setup
You’ll need an OpenAI API key:
```bash
export OPENAI_API_KEY=sk-...your_key...
```

## Usage
Start with:
```bash
xplain --help
```
Then try:
```bash
xplain ls
xplain chmod +x --funny
xplain grep --short
```