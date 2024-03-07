import unittest
from unittest.mock import patch, MagicMock
from your_module import fetch_credentials  # Adjust this import based on your actual file structure

class TestFetchCredentials(unittest.TestCase):
    @patch('your_module.requests.get')
    def test_fetch_credentials_success(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200, json=lambda: {"password": "secret"})
        result = fetch_credentials("testuser")
        self.assertEqual(result, {"Content": "secret"})

    @patch('your_module.requests.get')
    def test_user_not_found(self, mock_get):
        mock_get.return_value = MagicMock(status_code=404)
        result = fetch_credentials("nonexistentuser")
        self.assertEqual(result, {"Error": "User not found"})

    @patch('your_module.requests.get')
    def test_http_error(self, mock_get):
        mock_get.side_effect = requests.HTTPError("Internal Server Error", response=MagicMock(status_code=500))
        result = fetch_credentials("testuser")
        self.assertTrue("Error" in result)

    @patch('your_module.requests.get')
    def test_generic_exception(self, mock_get):
        mock_get.side_effect = Exception("Generic Error")
        result = fetch_credentials("testuser")
        self.assertTrue("Error" in result)

if __name__ == '__main__':
    unittest.main()
