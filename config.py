# config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-4"
MAX_TOKENS = 500
TEMPERATURE = 0.7

# Other imports and configurations
TOPIC = "Introduction to ANOVA"
