from typing import Optional

import requests
from SingleLog import DefaultLogger as Logger

logger = Logger('api-utils')


def req(method: str, url: str, data: dict = None, timeout: int = 10, headers: Optional[dict] = None):
    """Send request to PTT API server.

    Args:
        url (str): URL of the API endpoint.
        method (str): HTTP method.
        data (dict): Data to send in the request body.
        headers (dict): HTTP headers.
        timeout (int): Request timeout.

    Returns:
        dict: Response data.
    """

    if headers is None:
        headers = {}

    r = requests.request(method.upper(), url, data=data, headers=headers, timeout=timeout)
    if r.status_code != 200:
        logger.error(f'HTTP {method} {url} failed. Status code: {r.status_code}')
        raise None
    return r.json()
