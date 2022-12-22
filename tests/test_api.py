from SingleLog import DefaultLogger as Logger

from ptt_api_sdk.api import PttAPI

logger = Logger('test')


def test():
    api = PttAPI('token')

    logger.info('version api', api.version())
    logger.info('uservisitcount api', api.uservisitcount())


if __name__ == '__main__':
    test()
