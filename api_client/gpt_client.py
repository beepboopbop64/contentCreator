import openai
import os
from dotenv import load_dotenv


class GPTClient:
    """
    A client to interact with the OpenAI GPT API.
    """

    def __init__(self, api_key=None):
        """
        Initialize the GPTClient with an API key.

        Parameters:
        api_key (str): OpenAI API key. If not provided, it is fetched from the environment variable `OPENAI_API_KEY`.
        """
        load_dotenv()  # Load environment variables from a .env file
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def generate_text(self, prompt: str, max_tokens: int = 150) -> str:
        """
        Generate text based on the provided prompt.

        Parameters:
        prompt (str): The prompt to send to GPT.
        max_tokens (int): The maximum number of tokens to generate. Default is 150.

        Returns:
        str: The generated text.
        """
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=max_tokens,
                n=1,
                stop=None,
                temperature=0.7,
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"An error occurred while generating text: {e}")
            return ""
