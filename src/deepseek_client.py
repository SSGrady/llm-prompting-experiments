# deepseek_client.py
import os
from dataclasses import dataclass
from openai import OpenAI

@dataclass
class APIConfig:
    """ Configuration for Deepseek API connection.
    
    Attributes:
        base_url: Base API endpoint URL
        api_key: Authentication key from environment variable
        model: Model identifier for completions
        temperature: Sampling temp ranges from 0.0 - 1.0
    """
    base_url: str = "https://api.deepseek.com"
    api_key: str = os.getenv("DEEPSEEK_API_KEY")
    model: str = "deepseek-chat"
    temperature: float = 0.3

class DeepseekClient:
    """ Client for interacting with Deepseek's chat API.

    Handles authentication, request formation, and response processing.
    
    Args:
        config: APIConfig instance with connection parameters
    """
    def __init__(self, config: APIConfig):
        self.client = OpenAI(api_key=config.api_key, base_url=config.base_url)
        self.config = config
    
    def generate_response(self, system_prompt: str, user_prompt: str) -> str:
        """Generates a completion using configured model.

        Args:
            system_prompt: Role definition for the assistant
            user_prompt: User's input/question
        
        Returns:
            Raw text response from API

        Raises:
            RuntimeError: If API request fails. See docs for error codes
            https://api-docs.deepseek.com/quick_start/error_codes
        """
        try:
            response = self.client.chat.completions.create(
                model=self.config.model
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=self.config.temperature,
                stream=False
            )
            return response.choices[0].message.content
        except Exception as e:
            raise RuntimeError(f"API request failed: {str(e)}") from e