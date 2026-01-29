# CrewAI Getting Started (Free Model)

This is a minimal CrewAI starter project wired to a free, local model via Ollama.

## Prerequisites

- Python 3.10+
- [Ollama](https://ollama.com) installed and running

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Pull a free model with Ollama (example: Llama 3.1 8B):

```bash
ollama pull llama3.1
```

## Run

```bash
python main.py
```

## Notes

- The `.env` file points CrewAI to Ollama's OpenAI-compatible endpoint.
- You can swap the model by changing `OPENAI_MODEL_NAME` in `.env`.
