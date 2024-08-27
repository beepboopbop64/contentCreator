import openai
from openai import OpenAIError
from config import OPENAI_API_KEY, MODEL_NAME, MAX_TOKENS, TEMPERATURE, BLOG_POST_STRUCTURE, VIDEO_SCRIPT_STRUCTURE, TOPICS, IS_SERIES, SERIES_TITLE, SERIES_PART, EXAMPLE, TONE
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

    def construct_prompt(self, base_prompt: str, topic: str, series_title: str = None, part: str = None) -> str:
        """
        Construct the prompt for the GPT model, including series information, tone, and examples if applicable.
        """
        prompt = f"{base_prompt} {topic} in a {TONE} tone."
        if series_title and part:
            prompt = f"{series_title} - {part}: {prompt}"
        if EXAMPLE:
            prompt += f" Please include this example: {EXAMPLE}"
        return prompt

    def generate_section(self, prompt: str, max_tokens: int = MAX_TOKENS, temperature: float = TEMPERATURE) -> str:
        """
        Generate text for a specific section based on the provided prompt using the OpenAI GPT model.
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
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        if IS_SERIES:
            self._generate_series_blog_posts(topics, output_dir)
        else:
            self._generate_standalone_blog_posts(topics, output_dir)

    def generate_and_save_video_scripts(self, topics=TOPICS, output_dir="output/video_scripts"):
        """
        Generate complete video scripts for each topic in the topics list and save them to files.
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)

        if IS_SERIES:
            self._generate_series_video_scripts(topics, output_dir)
        else:
            self._generate_standalone_video_scripts(topics, output_dir)

    def _generate_series_blog_posts(self, topics, output_dir):
        """
        Generate a series of blog posts, saving each one with the correct series title and part.
        """
        for i, topic in enumerate(topics):
            series_title = SERIES_TITLE
            part = SERIES_PART[i] if i < len(SERIES_PART) else f"Part {i + 1}"

            sections = []
            for section_name, section_prompt in BLOG_POST_STRUCTURE.items():
                content = self.generate_section(self.construct_prompt(section_prompt, topic, series_title=series_title, part=part))
                sections.append(f"{section_name.capitalize()}:\n{content}\n")

            file_name = f"{topic.replace(' ', '_')}_part_{i + 1}.txt"
            file_path = os.path.join(output_dir, file_name)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write("\n".join(sections))
            print(f"Blog post for '{topic}' in series '{series_title}' saved to {file_path}")

    def _generate_standalone_blog_posts(self, topics, output_dir):
        """
        Generate standalone blog posts, saving each one individually.
        """
        for topic in topics:
            sections = []
            for section_name, section_prompt in BLOG_POST_STRUCTURE.items():
                content = self.generate_section(self.construct_prompt(section_prompt, topic))
                sections.append(f"{section_name.capitalize()}:\n{content}\n")

            file_name = f"{topic.replace(' ', '_')}.txt"
            file_path = os.path.join(output_dir, file_name)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write("\n".join(sections))
            print(f"Blog post for '{topic}' saved to {file_path}")

    def _generate_series_video_scripts(self, topics, output_dir):
        """
        Generate a series of video scripts, saving each one with the correct series title and part.
        """
        for i, topic in enumerate(topics):
            series_title = SERIES_TITLE
            part = SERIES_PART[i] if i < len(SERIES_PART) else f"Part {i + 1}"

            sections = []
            for section_name, section_prompt in VIDEO_SCRIPT_STRUCTURE.items():
                content = self.generate_section(self.construct_prompt(section_prompt, topic, series_title=series_title, part=part))
                sections.append(f"{section_name.capitalize()}:\n{content}\n")

            file_name = f"{topic.replace(' ', '_')}_script_part_{i + 1}.txt"
            file_path = os.path.join(output_dir, file_name)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write("\n".join(sections))
            print(f"Video script for '{topic}' in series '{series_title}' saved to {file_path}")

    def _generate_standalone_video_scripts(self, topics, output_dir):
        """
        Generate standalone video scripts, saving each one individually.
        """
        for topic in topics:
            sections = []
            for section_name, section_prompt in VIDEO_SCRIPT_STRUCTURE.items():
                content = self.generate_section(self.construct_prompt(section_prompt, topic))
                sections.append(f"{section_name.capitalize()}:\n{content}\n")

            file_name = f"{topic.replace(' ', '_')}_script.txt"
            file_path = os.path.join(output_dir, file_name)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write("\n".join(sections))
            print(f"Video script for '{topic}' saved to {file_path}")
