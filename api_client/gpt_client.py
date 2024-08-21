import openai
from openai import OpenAIError
from config import OPENAI_API_KEY, MODEL_NAME, MAX_TOKENS, TEMPERATURE, BLOG_POST_STRUCTURE, VIDEO_SCRIPT_STRUCTURE


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

    def generate_section(self, prompt: str, max_tokens: int = MAX_TOKENS, temperature: float = TEMPERATURE) -> str:
        """
        Generate text for a specific section based on the provided prompt using the OpenAI GPT model.

        Parameters:
        - prompt (str): The prompt to send to the GPT model.
        - max_tokens (int): The maximum number of tokens to generate. Default is from config.
        - temperature (float): The sampling temperature. Default is from config.

        Returns:
        - str: The generated text from the GPT model.
        """
        try:
            response = openai.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return response.choices[0].message.content.strip()
        except OpenAIError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        return ""

    def generate_blog_post(self) -> str:
        """
        Generate a complete blog post based on the structure defined in config.py.

        Returns:
        - str: The complete blog post.
        """
        sections = []
        for section, prompt in BLOG_POST_STRUCTURE.items():
            content = self.generate_section(prompt)
            sections.append(f"{section.capitalize()}:\n{content}\n")
        return "\n".join(sections)

    def generate_video_script(self) -> str:
        """
        Generate a complete video script based on the structure defined in config.py.

        Returns:
        - str: The complete video script.
        """
        sections = []
        for section, prompt in VIDEO_SCRIPT_STRUCTURE.items():
            content = self.generate_section(prompt)
            sections.append(f"{section.capitalize()}:\n{content}\n")
        return "\n".join(sections)