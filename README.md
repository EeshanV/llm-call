# llm-call

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A tiny Python wrapper that calls Gemini under the hood, but lets you invoke it via either the native Gemini SDK or the OpenAI‑compatible endpoint.

## Requirements

* Python 3.12+
* `google-genai`
* `openai`

## Install

```bash
pip install git+https://github.com/EeshanV/llm-call.git@main
```

## Usage

```python
from llm_call import call_llm

cfg = {
  "model": "gemini-2.5-pro",         # your Gemini model
  "temperature": 0.5,
  "system_instruction": "You are a helpful assistant.",
  "file": "/path/to/file.pdf"  # optional, Gemini only
}

reply = call_llm(
  message="Explain quantum tunneling in simple terms.",
  apikey="YOUR_API_KEY",
  config=cfg,
  provider="openai"
)
print(reply)
```

### Config Options

* `model` (str)
* `temperature` (float)
* `system_instruction` (str) — defaults to “You are a helpful assistant.”
* `file` (str) — path to PDF, optional

## License

This project is licensed under the MIT License.