import unittest
from unittest.mock import patch, Mock
from api_client.gpt_client import GPTClient
from openai import OpenAIError


class TestGPTClient(unittest.TestCase):
    """
    Unit tests for the GPTClient class.
    """

    @patch("openai.chat.completions.create")
    def test_generate_text_success(self, mock_create):
        """
        Test that generate_text successfully returns generated text when the API call is successful.

        This test mocks the OpenAI API response to simulate a successful request and verifies that the
        generate_text method returns the correct text.
        """
        # Mocking the API response
        mock_create.return_value = Mock(choices=[Mock(message=Mock(content="This is a test response."))])

        client = GPTClient()
        response = client.generate_text("Test prompt")
        self.assertEqual(response, "This is a test response.")

    @patch("openai.chat.completions.create")
    def test_generate_text_openai_error(self, mock_create):
        """
        Test that generate_text handles OpenAI errors gracefully and returns an empty string.

        This test simulates an OpenAIError when the API is called and verifies that the method
        handles the error and returns an empty string.
        """
        mock_create.side_effect = OpenAIError("API call failed")

        client = GPTClient()
        response = client.generate_text("Test prompt")
        self.assertEqual(response, "")

    @patch("openai.chat.completions.create")
    def test_generate_text_generic_error(self, mock_create):
        """
        Test that generate_text handles generic errors gracefully and returns an empty string.

        This test simulates a generic exception when the API is called and verifies that the method
        handles the error and returns an empty string.
        """
        mock_create.side_effect = Exception("A generic error occurred")

        client = GPTClient()
        response = client.generate_text("Test prompt")
        self.assertEqual(response, "")


if __name__ == '__main__':
    unittest.main()
