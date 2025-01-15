import unittest
from unittest.mock import MagicMock
from gemini_functions import GeminiFunctions, encode_image, format_chat_message
from api_client import api_client

class TestGeminiFunctions(unittest.TestCase):
    def setUp(self):
        self.gemini_functions = GeminiFunctions()
        api_client.gemini_model = MagicMock()

    def test_upload_to_gemini(self):
        image = MagicMock()
        image.save = MagicMock()
        result = self.gemini_functions.upload_to_gemini(image)
        self.assertIsNotNone(result)

    def test_chat_with_gemini(self):
        user_input = "Hello"
        chat_history = []
        api_client.gemini_model.start_chat = MagicMock(return_value=MagicMock())
        api_client.gemini_model.start_chat().send_message = MagicMock(return_value=MagicMock(text="Hi"))

        result = list(self.gemini_functions.chat_with_gemini(user_input, chat_history))
        self.assertEqual(result[0][0][1], "Hi")

    def test_analyze_image_gemini(self):
        image = MagicMock()
        user_input = "Describe this image"
        chat_history = []
        api_client.gemini_model.generate_content = MagicMock(return_value=[MagicMock(text="Image description")])

        result = self.gemini_functions.analyze_image_gemini(image, chat_history, user_input)
        self.assertIn("Image description", result[-1][1])

    def test_format_code(self):
        code_input = "print('Hello, world!')"
        result = self.gemini_functions.format_code(code_input)
        self.assertIn("<pre>", result)

    def test_save_code(self):
        code_input = "print('Hello, world!')"
        filename = "test_code.py"
        self.gemini_functions.save_code(code_input, filename)
        with open(filename, 'r') as file:
            content = file.read()
        self.assertIn("print('Hello, world!')", content)
        os.remove(filename)

    def test_load_code(self):
        filename = "test_code.py"
        with open(filename, 'w') as file:
            file.write("print('Hello, world!')")
        result = self.gemini_functions.load_code(filename)
        self.assertIn("print('Hello, world!')", result)
        os.remove(filename)

    def test_format_code_with_black(self):
        code_input = "print('Hello, world!')"
        result = self.gemini_functions.format_code_with_black(code_input)
        self.assertIn("print('Hello, world!')", result)

    def test_analyze_code(self):
        code_input = "print('Hello, world!')"
        api_client.gemini_model.generate_content = MagicMock(return_value=MagicMock(text="Code analysis"))
        result = self.gemini_functions.analyze_code(code_input)
        self.assertIn("Code analysis", result)

    def test_suggest_code_improvements(self):
        code_input = "print('Hello, world!')"
        api_client.gemini_model.generate_content = MagicMock(return_value=MagicMock(text="Code improvements"))
        result = self.gemini_functions.suggest_code_improvements(code_input)
        self.assertIn("Code improvements", result)

    def test_update_model(self):
        model_name = "gemini-pro"
        self.gemini_functions.update_model(model_name)
        self.assertEqual(api_client.gemini_model.model_name, model_name)

if __name__ == "__main__":
    unittest.main()
