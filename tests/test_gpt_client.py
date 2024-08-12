import unittest
from unittest.mock import patch, mock_open
from api_client.gpt_client import GPTClient


class TestGPTClient(unittest.TestCase):
    """
    Unit tests for the GPTClient.
    """

    @patch("api_client.gpt_client.load_dotenv")
    @patch("os.getenv")
    def test_api_key_loaded_from_env_file(self, mock_getenv, mock_load_dotenv):
        """
        Test that the API key is correctly loaded from a .env file.
        """
        mock_getenv.return_value = "test_api_key"
        client = GPTClient()

        mock_load_dotenv.assert_called_once()
        mock_getenv.assert_called_with("OPENAI_API_KEY")
        self.assertEqual(client.api_key, "test_api_key")

    @patch("openai.Completion.create")
    def test_generate_text_success(self, mock_create):
        """
        Test that generate_text successfully returns generated text when the API call is successful.
        """
        # Mocking the API response to return a proper structure
        mock_create.return_value = unittest.mock.Mock(
            choices=[unittest.mock.Mock(text="This is a generated text.")]
        )

        client = GPTClient(api_key="test_api_key")
        prompt = "Test prompt"
        response = client.generate_text(prompt)

        self.assertEqual(response, "This is a generated text.")

    @patch("openai.Completion.create")
    def test_generate_text_error(self, mock_create):
        """
        Test that generate_text handles errors gracefully and returns an empty string.
        """
        mock_create.side_effect = Exception("API call failed")
        client = GPTClient(api_key="test_api_key")
        prompt = "Test prompt"
        response = client.generate_text(prompt)

        self.assertEqual(response, "")


if __name__ == '__main__':
    unittest.main()
