import unittest
from unittest.mock import patch, MagicMock
import requests
import my_module  # Replace with the name of your module where password_cybervault is defined

class TestPasswordCyberVault(unittest.TestCase):
    @patch.dict('os.environ', {
        'CERT_FILE_DIR': '/mock/path/to',
        'CCP_URL': 'https://mocked-url.com',
        'EPV_APP_ID': 'mocked-app-id',
        'SAFE': 'mocked-safe'
    })
    @patch('my_module.requests.Session')
    @patch('my_module.can_force_ipv4')
    def test_password_cybervault(self, mock_can_force_ipv4, mock_session):
        # Setup mock for can_force_ipv4
        mock_can_force_ipv4.return_value = {'force': True}
        
        # Setup mock for requests.Session
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'Content': 'mocked-content'}
        
        mock_session.return_value.__enter__.return_value.get.return_value = mock_response
        
        # Call the function
        result = my_module.password_cybervault('mocked-user-name')
        
        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(result, {'Content': 'mocked-content'})
        
        # Ensure the session was called with the mocked cert and verify paths
        mock_session.return_value.__enter__.return_value.get.assert_called_with(
            'https://mocked-url.com',
            params={'AppID': 'mocked-app-id', 'UserName': 'mocked-user-name', 'Safe': 'mocked-safe', 'Reason': 'Fetch password'},
            cert=('/mock/path/to/cert-pem', '/mock/path/to/key-pem'),
            verify='/mock/path/to/certchain.pem'
        )

if __name__ == '__main__':
    unittest.main()
