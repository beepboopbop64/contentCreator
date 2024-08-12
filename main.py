from generators.blog_post_generator import generate_outline, generate_content, format_blog_post


def create_blog_post(topic: str):
    # Step 1: Generate the outline
    outline = generate_outline(topic)

    # Step 2: Generate the content using the GPT API
    content = generate_content(outline, topic)

    # Step 3: Format the content into a complete blog post
    formatted_post = format_blog_post(content)

    return formatted_post


if __name__ == '__main__':
    topic = "t-tests"
    blog_post = create_blog_post(topic)
    print(blog_post)
