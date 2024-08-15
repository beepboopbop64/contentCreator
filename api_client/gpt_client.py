import openai
from openai import OpenAIError
from config import OPENAI_API_KEY, MODEL_NAME, MAX_TOKENS, TEMPERATURE

class GPTClient:
    """
    A client to interact with the OpenAI GPT API.
    """

    def __init__(self):
        """
        Initialize the GPTClient with an API key.
        """
        if not OPENAI_API_KEY:
            raise ValueError("OpenAI API key not found. Please set the 'OPENAI_API_KEY' in your .env file.")
        openai.api_key = OPENAI_API_KEY

    def generate_text(self, prompt: str, max_tokens: int = MAX_TOKENS, temperature: float = TEMPERATURE) -> str:
        """
        Generate text based on the provided prompt using the OpenAI GPT model.

        Parameters:
        - prompt (str): The prompt to send to the GPT model.
        - max_tokens (int): The maximum number of tokens to generate. Default is from config.
        - temperature (float): The sampling temperature. Default is from config.

        Returns:
        - str: The generated text from the GPT model.
        """
        try:
            response = openai.chat.completions.create(
                model=MODEL_NAME,  # Specify the model from config
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return response.choices[0].message.content
        except OpenAIError as e:
            # Handle all OpenAI API errors
            print(f"Error: {e}")
        except Exception as e:
            # Handle non-OpenAI errors
            print(f"An unexpected error occurred: {e}")
        return ""
