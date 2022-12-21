import requests
from SingleLog import DefaultLogger as Logger, LogLevel


class PttAPI(object):
    """PttAPI is a class to access PTT API."""

    def __init__(self, access_token: str, endpoint: str = 'https://api.devptt.dev', timeout: int = 5):

        # api doc: https://doc.devptt.dev/

        self.logger = Logger(
            'Ptt API',
            LogLevel.DEBUG
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
        self.logger.info('Endpoint:', f'{self.endpoint}/version')
        try:
            response = requests.get(f'{self.endpoint}/version', timeout=self.timeout)
            response.encoding = 'utf-8'
        except requests.exceptions.HTTPError as err:
            self.logger.error(err)
            return None

        if response.status_code != 200:
            self.logger.error(f'Get PTT API version failed. Status code: {response.status_code}')
            return None

        self.logger.info('Get PTT API version success.')
        self.logger.debug(f'PTT API version: {response.text}')

        with open('version.html', 'w') as f:
            f.write(response.text)

        return response.json()
