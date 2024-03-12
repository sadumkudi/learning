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

# ============================


import unittest
from unittest.mock import patch
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException

# Assuming your function is defined in mymodule.py
from mymodule import get_password_from_cv

class TestGetPasswordFromCV(unittest.TestCase):

    @patch('mymodule.requests.get')
    def test_http_error(self, mock_get):
        # Configure the mock to raise an HTTPError.
        mock_get.side_effect = HTTPError('HTTP Error occurred')
        
        # Call the function and verify it handles HTTPError as expected.
        with self.assertRaises(HTTPError):
            get_password_from_cv()

    @patch('mymodule.requests.get')
    def test_connection_error(self, mock_get):
        # Configure the mock to raise a ConnectionError.
        mock_get.side_effect = ConnectionError('Connection Error occurred')
        
        # Call the function and verify it handles ConnectionError as expected.
        with self.assertRaises(ConnectionError):
            get_password_from_cv()

    @patch('mymodule.requests.get')
    def test_timeout(self, mock_get):
        # Configure the mock to raise a Timeout exception.
        mock_get.side_effect = Timeout('Timeout occurred')
        
        # Call the function and verify it handles Timeout as expected.
        with self.assertRaises(Timeout):
            get_password_from_cv()

    @patch('mymodule.requests.get')
    def test_request_exception(self, mock_get):
        # Configure the mock to raise a RequestException.
        mock_get.side_effect = RequestException('General RequestException occurred')
        
        # Call the function and verify it handles RequestException as expected.
        with self.assertRaises(RequestException):
            get_password_from_cv()

# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main()
