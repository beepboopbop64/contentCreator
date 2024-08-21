from api_client.gpt_client import GPTClient


def main():
    client = GPTClient()

    # Generate a blog post
    blog_post = client.generate_blog_post()
    print("Generated Blog Post:")
    print(blog_post)

    # Generate a video script
    # video_script = client.generate_video_script()
    # print("Generated Video Script:")
    # print(video_script)


if __name__ == "__main__":
    main()
