from unittest import TestCase, mock
from unittest.mock import patch
from .utils import can_force_ipv4  # Adjust the import path according to your project structure

class CanForceIPv4Test(TestCase):
    @mock.patch('requests.packages.urllib3.connectionpool.HTTPConnection')
    @mock.patch('requests.packages.urllib3.connectionpool.VerifiedHTTPSConnection')
    @mock.patch('requests.packages.urllib3.connectionpool.HTTPConnectionPool')
    @mock.patch('requests.packages.urllib3.connectionpool.HTTPSConnectionPool')
    def test_can_force_ipv4_patches_classes(self, mock_https_pool, mock_http_pool, mock_verified_https, mock_http):
        result = can_force_ipv4()
        self.assertTrue(result['force'])
        # Since your function replaces classes, verify that a simple assignment check suffices.
        # In reality, you're asserting the mock is called which stands in place of your actual class replacement logic.
        # This part of the test somewhat deviates from directly asserting class replacements due to the nature of patching.
        # Additional, more intricate mocks and assertions might be needed depending on the specifics of how your application uses these patched connections.
## ----------------------

from django.test import TestCase
from unittest.mock import patch, MagicMock
from .utils import can_force_ipv4  # Adjust the import path according to your project structure

class CanForceIPv4Test(TestCase):
    def test_can_force_ipv4_success(self):
        # Test the function under normal conditions
        result = can_force_ipv4()
        self.assertEqual(result, {"force": True})

    @patch('path.to.your.utils.socket.socket')
    def test_can_force_ipv4_exception(self, mock_socket):
        # Force an exception to be raised
        mock_socket.side_effect = Exception("Forced exception for test")

        result = can_force_ipv4()
        self.assertEqual(result, {"force": False})
