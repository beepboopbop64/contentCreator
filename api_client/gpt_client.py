import openai
import os
from dotenv import load_dotenv
from openai import OpenAIError


class GPTClient:
    """
    A client to interact with the OpenAI GPT API.
    """

    def __init__(self):
        """
        Initialize the GPTClient with an API key from the .env file.

        The API key is loaded from the environment variable `OPENAI_API_KEY`
        which is expected to be defined in a `.env` file.
        """
        load_dotenv()  # Load environment variables from the .env file
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key not found. Please set the 'OPENAI_API_KEY' in your .env file.")
        openai.api_key = self.api_key

    def generate_text(self, prompt: str, max_tokens: int = 500) -> str:
        """
        Generate text based on the provided prompt using the OpenAI GPT model.

        Parameters:
        - prompt (str): The prompt to send to the GPT model.
        - max_tokens (int): The maximum number of tokens to generate. Default is 150.

        Returns:
        - str: The generated text from the GPT model.
        """
        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",  # Specify the model, e.g., "gpt-3.5-turbo" or "gpt-4"
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content
        except OpenAIError as e:
            # Handle all OpenAI API errors
            print(f"Error: {e}")
        except Exception as e:
            # Handle non-OpenAI errors
            print(f"An unexpected error occurred: {e}")
        return ""
