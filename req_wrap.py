def request_wrap(method, url, **kwargs):
    """
    Sends an HTTP request using the specified method to the given URL with optional keyword arguments,
    ensuring that the request is verified against a custom certificate chain.

    The function dynamically selects the HTTP method (GET or POST) based on the 'method' parameter.
    It retrieves the directory of the certificate file from an environment variable named 'file_path',
    constructs the path to the certificate chain file ('certchain.pm'), and uses it to verify the SSL
    connection.

    Parameters:
    - method (str): The HTTP method to use for the request. Supported methods: 'get', 'post'.
    - url (str): The URL to which the request will be sent.
    - **kwargs: Arbitrary keyword arguments that are passed directly to the underlying requests method.
      These could include parameters like headers, data, json, etc.

    Returns:
    - requests.Response: The response object from the requests library, which contains the server's response to the HTTP request.

    Raises:
    - requests.exceptions.RequestException: An error occurred during the request. This could be a connection error, timeout, etc.

    Note:
    - The function assumes the presence of an environment variable 'file_path' that contains the directory path of the certificate file.
    - The certificate chain file 'certchain.pm' must be present in the specified directory.
    - Currently, only GET and POST methods are supported. If a different method is specified, the function will not execute an HTTP request.
    """
    cert_file_dir = os.getenv('file_path')
    cert_chain = os.path.join(cert_file_dir, 'certchain.pm')

    if method == 'get':
        res = requests.get(url, verify=cert_chain, **kwargs)
    elif method == 'post':
        res = requests.post(url, verify=cert_chain, **kwargs)

    return res
