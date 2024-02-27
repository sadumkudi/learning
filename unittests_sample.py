# Assuming your function is in myproject/utils/utils.py
from unittest import TestCase
from unittest.mock import patch, MagicMock
from myproject.utils.utils import get_passwd_cyberArk

class TestGetPasswdCyberArk(TestCase):

    @patch('myproject.utils.utils.requests.get')  # Mock the requests.get call
    @patch('builtins.open', new_callable=MagicMock)  # Mock the open function
    def test_get_passwd_cyberArk(self, mock_open, mock_get):
        # Mock the response of the CyberArk REST API call
        mock_response = MagicMock()
        mock_response.json.return_value = {'password': 'secretPassword123'}
        mock_get.return_value = mock_response

        # Define your test parameters
        test_rest_url = 'https://cyberark.example.com'
        test_query_params = {'query': 'param'}
        test_file_dir = '/path/to/cert'

        # Call the function with the test parameters
        result = get_passwd_cyberArk(test_rest_url, test_query_params, test_file_dir)

        # Verify the function's behavior and outcome
        self.assertEqual(result, 'secretPassword123')
        mock_get.assert_called_once_with(test_rest_url, params=test_query_params, verify=test_file_dir)
        mock_open.assert_called()  # Add more specific assertions here if necessary


@patch('ddi_api.utils.requests.Session.get')
def test_get_password_cybervault_failure(self, mock_session):
    mock_response = mock_session.return_value.get.return_value
    # Simulate a failure response from the API, e.g., 404 Not Found
    mock_response.status_code = 404
    # Optionally, you can provide a mock response body for specific error scenarios
    mock_response.json.return_value = {"error": "Resource not found"}
    mock_session.return_value = mock_response

    response = get_password_cybervault()

    # Assuming your function returns None or a specific message/format in case of failure
    # Adjust the expected response based on your function's actual failure handling
    self.assertIsNone(response)  # or self.assertEqual(response, expected_failure_response)
