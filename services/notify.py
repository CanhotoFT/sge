import requests


class Notify:

    def __init__(self):
        self.__base_url = 'https://webhook.site'

    def send_event(self, data):
        requests.post(
            url = f'{self.__base_url}/c1f148f5-73ab-4147-a2fc-145a3e8593c9',
            json = data,
        )
