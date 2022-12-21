from ptt_api_sdk.api import PttAPI


def test():
    api = PttAPI('token')

    print(api.version())


if __name__ == '__main__':
    test()
