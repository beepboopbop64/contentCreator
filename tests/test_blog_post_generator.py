import unittest
from generators.blog_post_generator import generate_outline, generate_content, format_blog_post


class TestBlogPostGenerator(unittest.TestCase):
    """
    Unit tests for the blog post generator.
    """

    def test_generate_outline_valid_topic(self):
        """
        Test that generate_outline returns a dictionary with keys 'introduction', 'body', and 'conclusion'
        when provided with a valid topic.
        """
        topic = "Introduction to ANOVA"
        outline = generate_outline(topic)

        expected_keys = ['introduction', 'body', 'conclusion']
        self.assertIsInstance(outline, dict)
        self.assertTrue(all(key in outline for key in expected_keys))
        self.assertTrue(all(outline[key] == "" for key in expected_keys))

    def test_generate_outline_empty_topic(self):
        """
        Test that generate_outline returns an empty dictionary when provided with an empty topic.
        """
        topic = ""
        outline = generate_outline(topic)

        self.assertEqual(outline, {})

    def test_generate_content_valid_outline(self):
        """
        Test that generate_content returns a dictionary with filled content for a valid outline.
        """
        outline = {
            'introduction': '',
            'body': '',
            'conclusion': ''
        }
        topic = "Introduction to ANOVA"
        content = generate_content(outline, topic)

        self.assertIsInstance(content, dict)
        self.assertTrue(len(content['introduction']) > 0)
        self.assertTrue(len(content['body']) > 0)
        self.assertTrue(len(content['conclusion']) > 0)

    def test_generate_content_empty_outline(self):
        """
        Test that generate_content returns an empty dictionary when provided with an empty outline.
        """
        outline = {}
        topic = "Introduction to ANOVA"
        content = generate_content(outline, topic)

        self.assertEqual(content, {})

    def test_format_blog_post_valid_content(self):
        """
        Test that format_blog_post returns a properly formatted blog post when given valid content.
        """
        content = {
            'introduction': "This is the introduction.",
            'body': "This is the body.",
            'conclusion': "This is the conclusion."
        }
        formatted_post = format_blog_post(content)

        self.assertIsInstance(formatted_post, str)
        self.assertIn("Introduction:", formatted_post)
        self.assertIn("This is the introduction.", formatted_post)
        self.assertIn("Body:", formatted_post)
        self.assertIn("This is the body.", formatted_post)
        self.assertIn("Conclusion:", formatted_post)
        self.assertIn("This is the conclusion.", formatted_post)

    def test_format_blog_post_empty_content(self):
        """
        Test that format_blog_post returns an empty string when given empty content.
        """
        content = {}
        formatted_post = format_blog_post(content)

        self.assertEqual(formatted_post, "")


if __name__ == '__main__':
    unittest.main()
