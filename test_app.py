import unittest
from flask_app import app
import urllib.parse


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to BookBuddy!", response.data)

    def test_recommend_title(self):
        # Ensure the title exists in your dataset
        response = self.app.get("/recommend?title=Known Title")
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on expected output

    def test_recommend_author(self):
        # URL encode the author name
        author_name = "J.K. Rowling"
        encoded_author_name = urllib.parse.quote_plus(author_name)

        # Make the test request
        response = self.app.get(f"/recommend?authors={encoded_author_name}")

        # Check if response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
