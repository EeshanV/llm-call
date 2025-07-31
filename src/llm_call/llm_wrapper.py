# src/llm_call/llm_wrapper.py

import pathlib
from typing import Dict, Any

# Gemini
from google import genai
from google.genai import types as gtypes

# OpenAI
from openai import OpenAI as OpenAIClient

default_sys = "You are a helpful assisstant."
def call_llm(user_prompt: str, apikey:str, config: Dict[str, Any], provider: str) -> str:
    provider = provider.lower()
    if provider == "gemini":
        client = genai.Client(api_key=apikey)
        
        file_path = config.get("file")
        contents=[user_prompt]
        if file_path:
            file = pathlib.Path(file_path)
            if not file.exists():
                raise FileNotFoundError(f"No such file: {file_path}")
            encoded_file = gtypes.Part.from_bytes(
                data=file.read_bytes(),
                mime_type='application/pdf'
            )
            contents.append(encoded_file)
            
        generate_content_config = gtypes.GenerateContentConfig(
            temperature=config.get("temperature", 0.5),
            system_instruction=config.get("system_instruction",default_sys),
        )
        try:
            response = client.models.generate_content(
                contents=contents,
                config=generate_content_config,
                model=config.get("model")
            )
            return response.text
        except Exception as e:
            raise RuntimeError(f"Gemini API error {e}") from e
    
    elif provider == "openai":
        client = OpenAIClient(api_key=apikey, base_url="http://localhost:8000/v1")
        try:
            response = client.chat.completions.create(
                model=config.get("model"),
                messages=[{"role": "user", "content": config.get("system_instruction", default_sys)},
                          {"role": "user", "content": user_prompt}],
                temperature=config.get("temperature", 0.5)
            )
            return response.choices[0].message.content
        except Exception as e:
            raise RuntimeError(f"OpenAI API error: {e}") from e
    
    else:
        raise ValueError("'provider' must be either 'gemini' or 'openai'")
