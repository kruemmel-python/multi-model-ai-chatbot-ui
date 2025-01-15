
import unittest
from unittest.mock import MagicMock
from mistral_functions import MistralFunctions, encode_image, format_chat_message
from api_client import api_client

class TestMistralFunctions(unittest.TestCase):
    def setUp(self):
        self.mistral_functions = MistralFunctions()
        api_client.mistral_client = MagicMock()

    def test_chat_with_mistral(self):
        user_input = "Hello"
        chat_history = []
        api_client.mistral_client.chat.complete = MagicMock(return_value=MagicMock(choices=[MagicMock(message=MagicMock(content="Hi"))]))

        result = list(self.mistral_functions.chat_with_mistral(user_input, chat_history))
        self.assertEqual(result[0][0][1], "Hi")

    def test_analyze_image_mistral(self):
        image = MagicMock()
        user_input = "Describe this image"
        chat_history = []
        api_client.mistral_client.chat.complete = MagicMock(return_value=MagicMock(choices=[MagicMock(message=MagicMock(content="Image description"))]))

        result = self.mistral_functions.analyze_image_mistral(image, chat_history, user_input, "Describe this image")
        self.assertIn("Image description", result[-1][1])

    def test_compare_images_mistral(self):
        image1 = MagicMock()
        image2 = MagicMock()
        chat_history = []
        api_client.mistral_client.chat.complete = MagicMock(return_value=MagicMock(choices=[MagicMock(message=MagicMock(content="Image comparison"))]))

        result = self.mistral_functions.compare_images_mistral(image1, image2, chat_history)
        self.assertIn("Image comparison", result[-1][1])

if __name__ == "__main__":
    unittest.main()
