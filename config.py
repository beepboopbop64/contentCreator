import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-3.5-turbo"  # gpt-4
MAX_TOKENS = 500
TEMPERATURE = 0.7

# Other imports and configurations
TOPIC = "Introduction to ANOVA"

# Tone Dictionary Based on Content Creators
TONE_DICTIONARY = {
    "sentdex": "The tone should be technical and educational, with a clear step-by-step coding walkthrough, including practical examples and explanations for each step",
    "kyla": "Use relatable analogies and storytelling to simplify the topic, making the content accessible and interesting to a general audience"
}

# Select the content creator's tone you want to use
CONTENT_CREATOR = "kyla"
TONE = TONE_DICTIONARY.get(CONTENT_CREATOR)

# Optional example to be included
EXAMPLE = None


# Function to construct the prompt with optional example
def construct_prompt(base_prompt):
    if EXAMPLE:
        return f"{base_prompt} Please include this example: {EXAMPLE}"
    return base_prompt


# Blog Post Structure with Topic, Tone, and Conditional Example Included
BLOG_POST_STRUCTURE = {
    "introduction": construct_prompt(f"Write an engaging introduction about {TOPIC}. {TONE}."),
    "body": construct_prompt(f"Provide detailed information and analysis on {TOPIC}. {TONE}."),
    "conclusion": construct_prompt(f"Summarize the key points and provide a concluding thought about {TOPIC}. {TONE}.")
}

# Video Script Structure with Topic, Tone, and Conditional Example Included
VIDEO_SCRIPT_STRUCTURE = {
    "intro": construct_prompt(f"Create an engaging introduction for a video about {TOPIC}.{TONE}."),
    "key_points": construct_prompt(f"Outline the main points that will be discussed in a video about {TOPIC}. {TONE}."),
    "summary": construct_prompt(f"Provide a concise summary of the content covered in the video about {TOPIC}. {TONE}.")
}
