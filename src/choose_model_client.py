# choose_model_client.py

from dotenv import load_dotenv
import os
from dataclasses import dataclass
from openai import OpenAI, OpenAIError

load_dotenv()
""" Configuration for model API connection.

Attributes:

base_url: Base API endpoint URL

deepseek_api_key: Fallback authentication key from environment variable

openai_api_key: Authentication key, more expensive and reliable

model: Model identifier for completions

fallback_model: Fallback model identifier for completions

temperature: Sampling temp ranges from 0.0 - 1.0

"""
@dataclass
class APIConfig:
    base_url: str = "https://api.deepseek.com"
    deepseek_api_key: str = os.getenv("DEEPSEEK_API_KEY")
    openai_api_key: str = os.getenv("OPENAI_API_KEY") 
    model: str = "deepseek-chat"
    fallback_model: str = "gpt-4o"
    temperature: float = 0.2

class OpenAIClient:
    def __init__(self, config: APIConfig):
        self.config = config
        
        # If we have a Deepseek key, create a "deepseek" client with base_url.
        # If not, just store None.
        self.deepseek_client = (
            OpenAI(api_key=config.deepseek_api_key, base_url=config.base_url)
            if config.deepseek_api_key
            else None
        )
        
        # If we have an OpenAI key, create a fallback or primary "openai" client
        # with the default base_url from openai package. If not, store None.
        self.openai_client = (
            OpenAI(api_key=config.openai_api_key)
            if config.openai_api_key
            else None
        )
    
    def request_deepseek(self, system_prompt: str, user_prompt: str) -> str:
        # Expects self.deepseek_client is not None
        try:
            response = self.deepseek_client.chat.completions.create(
                model=self.config.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=self.config.temperature,
                stream=False,
            )
            print("USED DEEPSEEK MODEL!\n")
            return response.choices[0].message.content
        except OpenAIError as e:
            # Return empty or raise so we know to fall back
            print(f"Deepseek request failed: {e}")
            return ""

    def request_openai(self, system_prompt: str, user_prompt: str) -> str:
        # Expects self.openai_client is not None
        response = self.openai_client.chat.completions.create(
            model=self.config.fallback_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=self.config.temperature,
            stream=False,
        )
        print("USED OPENAI CHATGPT MODEL!\n")
        return response.choices[0].message.content

    def generate_response(self, system_prompt: str, user_prompt: str) -> str:
        
        # 1) Use OpenAI if available
        if self.openai_client:
            return self.request_openai(system_prompt, user_prompt)
        
        # 1) If we have a Deepseek key (and client), try that next
        elif self.deepseek_client:
            content = self.request_deepseek(system_prompt, user_prompt)
            if content.strip():
                return content
        
        # 3) If we have neither, raise an error
        raise RuntimeError("No valid DEEPSEEK_API_KEY or OPENAI_API_KEY found.")
