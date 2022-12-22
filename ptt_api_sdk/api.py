import requests
from SingleLog import DefaultLogger as Logger, LogLevel

from ptt_api_sdk import utils


class PttAPI(object):
    """PttAPI is a class to access PTT API."""

    def __init__(self, access_token: str, endpoint: str = 'https://api.devptt.dev/api', timeout: int = 5):

        # api doc: https://doc.devptt.dev/

        self.logger = Logger(
            'Ptt API',
            # LogLevel.DEBUG
        )

        if not isinstance(access_token, str):
            raise TypeError('access_token must be str')
        self.access_token = access_token

        if not isinstance(endpoint, str):
            raise TypeError('endpoint must be str')
        self.endpoint = endpoint

        if not isinstance(timeout, int):
            raise TypeError('timeout must be int')
        self.timeout = timeout

    def version(self):
        """Get PTT API version from the endpoint."""

        self.logger.info('Get PTT API version from the endpoint.')
        self.logger.debug('Endpoint:', f'{self.endpoint}/version')

        response = utils.req('GET', f'{self.endpoint}/version', timeout=self.timeout)

        self.logger.debug('Response:', response)

        if response is None:
            self.logger.error('Endpoint:', f'{self.endpoint}/version', 'Response is None.')
            return None

        self.logger.info('Get PTT API version from the endpoint successfully.')
        return response

