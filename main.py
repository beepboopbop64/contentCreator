from api_client.gpt_client import GPTClient


def main():
    client = GPTClient()

    # Generate and save blog posts
    client.generate_and_save_blog_posts()

    # Generate and save video scripts
    # client.generate_and_save_video_scripts()


if __name__ == "__main__":
    main()
