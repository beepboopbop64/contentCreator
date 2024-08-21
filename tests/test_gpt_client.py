import unittest
from unittest.mock import patch, Mock
from api_client.gpt_client import GPTClient
from config import MAX_TOKENS, TEMPERATURE, TONE, TOPIC, BLOG_POST_STRUCTURE, VIDEO_SCRIPT_STRUCTURE
from openai import OpenAIError


class TestGPTClient(unittest.TestCase):
    """
    Unit tests for the GPTClient class.
    """

    @patch("openai.chat.completions.create")
    def test_generate_text_success(self, mock_create):
        """
        Test that generate_section successfully returns generated text when the API call is successful.
        """
        mock_create.return_value = Mock(choices=[Mock(message=Mock(content="This is a test response."))])

        client = GPTClient()
        prompt = BLOG_POST_STRUCTURE['introduction']
        response = client.generate_section(prompt, max_tokens=MAX_TOKENS, temperature=TEMPERATURE)
        self.assertEqual(response, "This is a test response.")

    @patch("openai.chat.completions.create")
    def test_generate_text_with_tone_and_example(self, mock_create):
        """
        Test that generate_section constructs the correct prompt including the tone and example.
        """
        mock_create.return_value = Mock(choices=[Mock(message=Mock(content="This is a test response."))])

        client = GPTClient()

        # Temporarily set EXAMPLE for this test
        example = "This is a specific example."
        expected_prompt = f"Write an engaging introduction about {TOPIC}. {TONE} Please include this example: {example}"

        # Construct prompt with the temporary example
        prompt = f"Write an engaging introduction about {TOPIC}. {TONE} Please include this example: {example}"
        response = client.generate_section(prompt, max_tokens=MAX_TOKENS, temperature=TEMPERATURE)

        mock_create.assert_called_once_with(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": expected_prompt}],
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
        )
        self.assertEqual(response, "This is a test response.")

    @patch("openai.chat.completions.create")
    def test_generate_text_openai_error(self, mock_create):
        """
        Test that generate_section handles OpenAI errors gracefully and returns an empty string.
        """
        mock_create.side_effect = OpenAIError("API call failed")

        client = GPTClient()
        prompt = BLOG_POST_STRUCTURE['introduction']
        response = client.generate_section(prompt, max_tokens=MAX_TOKENS, temperature=TEMPERATURE)
        self.assertEqual(response, "")

    @patch("openai.chat.completions.create")
    def test_generate_text_generic_error(self, mock_create):
        """
        Test that generate_section handles generic errors gracefully and returns an empty string.
        """
        mock_create.side_effect = Exception("A generic error occurred")

        client = GPTClient()
        prompt = BLOG_POST_STRUCTURE['introduction']
        response = client.generate_section(prompt, max_tokens=MAX_TOKENS, temperature=TEMPERATURE)
        self.assertEqual(response, "")

    def test_construct_prompt_with_example(self):
        """
        Test that construct_prompt correctly includes the example when defined.
        """
        from config import construct_prompt

        example = "This is a specific example."
        base_prompt = f"Write an engaging introduction about {TOPIC}. {TONE}"
        expected_prompt = f"{base_prompt} Please include this example: {example}"

        # Manually set EXAMPLE to simulate the configuration
        result = construct_prompt(base_prompt + f" Please include this example: {example}")
        self.assertEqual(result, expected_prompt)

    def test_construct_prompt_without_example(self):
        """
        Test that construct_prompt omits the example when it is not defined.
        """
        from config import construct_prompt

        base_prompt = f"Write an engaging introduction about {TOPIC}. {TONE}"
        result = construct_prompt(base_prompt)
        self.assertEqual(result, base_prompt)


if __name__ == '__main__':
    unittest.main()
