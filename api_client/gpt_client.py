import openai
from openai import OpenAIError
from config import OPENAI_API_KEY, MODEL_NAME, MAX_TOKENS, TEMPERATURE, BLOG_POST_STRUCTURE, VIDEO_SCRIPT_STRUCTURE, TOPICS
import os


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

    def generate_and_save_blog_posts(self, topics=TOPICS, output_dir="output/blog_posts"):
        """
        Generate complete blog posts for each topic in the topics list and save them to files.

        Parameters:
        - topics (list): List of topics to generate content for. Default is from config.
        - output_dir (str): Directory to save the output files.
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        for topic in topics:
            sections = []
            for section_name, section_prompt in BLOG_POST_STRUCTURE.items():
                content = self.generate_section(section_prompt(topic))
                sections.append(f"{section_name.capitalize()}:\n{content}\n")

            # Save to file using os.path.join to handle paths
            file_path = os.path.join(output_dir, f"{topic.replace(' ', '_')}.txt")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write("\n".join(sections))
            print(f"Blog post for '{topic}' saved to {file_path}")

    def generate_and_save_video_scripts(self, topics=TOPICS, output_dir="output/video_scripts"):
        """
        Generate complete video scripts for each topic in the topics list and save them to files.

        Parameters:
        - topics (list): List of topics to generate content for. Default is from config.
        - output_dir (str): Directory to save the output files.
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        for topic in topics:
            sections = []
            for section_name, section_prompt in VIDEO_SCRIPT_STRUCTURE.items():
                content = self.generate_section(section_prompt(topic))
                sections.append(f"{section_name.capitalize()}:\n{content}\n")

            # Save to file using os.path.join to handle paths
            file_path = os.path.join(output_dir, f"{topic.replace(' ', '_')}_script.txt")
            with open(file_path, "w", encoding="utf-8") as file:
                file.write("\n".join(sections))
            print(f"Video script for '{topic}' saved to {file_path}")
