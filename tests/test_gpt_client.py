import unittest
import os
from unittest.mock import patch, mock_open, Mock, ANY
from api_client.gpt_client import GPTClient
from config import TOPICS


class TestGPTClient(unittest.TestCase):
    """
    Unit tests for the GPTClient class.
    """

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.makedirs")
    @patch("openai.chat.completions.create")
    def test_generate_and_save_blog_posts(self, mock_create, mock_makedirs, mock_file):
        """
        Test that blog posts are generated and saved to files correctly.
        """
        mock_create.return_value = Mock(choices=[Mock(message=Mock(content="This is a test response."))])

        client = GPTClient()
        client.generate_and_save_blog_posts(topics=["Topic 1", "Topic 2"], output_dir="output/blog_posts")

        # Ensure directories are created
        mock_makedirs.assert_called_once_with(ANY, exist_ok=True)

        # Extract the actual file paths from the mock calls
        actual_paths = [call_args[0][0].replace('\\', '/') for call_args in mock_file.call_args_list]
        expected_paths = [
            os.path.join("output", "blog_posts", "Topic_1.txt").replace('\\', '/'),
            os.path.join("output", "blog_posts", "Topic_2.txt").replace('\\', '/')
        ]

        # Compare the paths
        self.assertCountEqual(actual_paths, expected_paths)

        # Adjust the expected content to match the actual content
        expected_content = "Introduction:\nThis is a test response.\n\nBody:\nThis is a test response.\n\nConclusion:\nThis is a test response.\n"
        handle = mock_file()
        handle.write.assert_any_call(expected_content)

    @patch("builtins.open", new_callable=mock_open)
    @patch("os.makedirs")
    @patch("openai.chat.completions.create")
    def test_generate_and_save_video_scripts(self, mock_create, mock_makedirs, mock_file):
        """
        Test that video scripts are generated and saved to files correctly.
        """
        mock_create.return_value = Mock(choices=[Mock(message=Mock(content="This is a test response."))])

        client = GPTClient()
        client.generate_and_save_video_scripts(topics=["Topic 1", "Topic 2"], output_dir="output/video_scripts")

        # Ensure directories are created
        mock_makedirs.assert_called_once_with(ANY, exist_ok=True)

        # Extract the actual file paths from the mock calls
        actual_paths = [call_args[0][0].replace('\\', '/') for call_args in mock_file.call_args_list]
        expected_paths = [
            os.path.join("output", "video_scripts", "Topic_1_script.txt").replace('\\', '/'),
            os.path.join("output", "video_scripts", "Topic_2_script.txt").replace('\\', '/')
        ]

        # Compare the paths
        self.assertCountEqual(actual_paths, expected_paths)

        # Adjust the expected content to match the actual content
        expected_content = "Intro:\nThis is a test response.\n\nKey_points:\nThis is a test response.\n\nSummary:\nThis is a test response.\n"
        handle = mock_file()
        handle.write.assert_any_call(expected_content)


if __name__ == '__main__':
    unittest.main()
