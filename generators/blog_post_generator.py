# content_generator/blog_post_generator.py
from api_client.gpt_client import GPTClient


def generate_outline(topic: str) -> dict:
    """
    Generate an outline for a blog post based on the provided topic.

    Parameters:
    topic (str): The topic of the blog post.

    Returns:
    dict: A dictionary with keys 'introduction', 'body', and 'conclusion'.
          Each key has an empty string as its value if the topic is valid.
          Returns an empty dictionary if the topic is empty.
    """
    if not topic:
        return {}

    return {
        'introduction': '',
        'body': '',
        'conclusion': ''
    }


def generate_content(outline: dict, topic: str) -> dict:
    """
    Generate content for a blog post based on the provided outline and topic using GPT.

    Parameters:
    outline (dict): A dictionary with keys 'introduction', 'body', 'conclusion'.
    topic (str): The topic of the blog post.

    Returns:
    dict: A dictionary with keys 'introduction', 'body', and 'conclusion' filled with content.
          Returns an empty dictionary if the outline is empty.
    """
    if not outline:
        return {}

    gpt_client = GPTClient()

    content = {
        'introduction': gpt_client.generate_text(f"Write an introduction about {topic}."),
        'body': gpt_client.generate_text(f"Explain the main concepts of {topic}."),
        'conclusion': gpt_client.generate_text(f"Summarize the importance of {topic}.")
    }

    return content


def format_blog_post(content: dict) -> str:
    """
    Format the content dictionary into a complete blog post.

    Parameters:
    content (dict): A dictionary with keys 'introduction', 'body', and 'conclusion' filled with content.

    Returns:
    str: A formatted blog post as a string. Returns an empty string if the content is empty.
    """
    if not content:
        return ""

    formatted_post = (
        f"Introduction:\n{content.get('introduction', '')}\n\n"
        f"Body:\n{content.get('body', '')}\n\n"
        f"Conclusion:\n{content.get('conclusion', '')}"
    )

    return formatted_post

