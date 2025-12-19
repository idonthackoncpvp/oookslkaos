from primp import Client
from util import Util

class Session:
    @staticmethod
    def session() -> Client:
        browsers = [
            ("chrome136", '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"', "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36")
        ]

        browser = browsers[0]
        proxy = Util.get_random_proxy()

        session = Client(
            impersonate="chrome_133",
            impersonate_os="windows",
            proxy=proxy,
            verify=False
        )

        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': f'{Util.get_random_string()};q=0.9,en;q=0.8',
            'content-type': 'application/json;charset=UTF-8',
            'origin': 'https://www.roblox.com',
            'priority': 'u=0, i',
            'sec-ch-ua': browser[1],
            'sec-ch-ua-mobile': "?0",
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': "document",
            'sec-fetch-user': "?1",
            'sec-fetch-mode': "navigate",
            'sec-fetch-site': "same-origin",
            'user-agent': browser[2],
            'upgrade-insecure-requests': '1'
        }

        session.headers = Util.sort_dict_order(headers)

        return session

    @staticmethod
    def set_page_request_headers(headers: dict) -> dict:
        headers.update({
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'priority': 'u=0, i',
            'sec-fetch-dest': 'document',
            'sec-fetch-user': '?1',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1'
        })

        return Util.sort_dict_order(headers)

    @staticmethod
    def set_iframe_request_headers(headers: dict) -> dict:
        headers.update({
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'priority': 'u=0, i',
            'sec-fetch-dest': 'iframe',
            'sec-fetch-user': '?1',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1'
        })

        return Util.sort_dict_order(headers)

    @staticmethod
    def set_image_request_headers(headers: dict) -> dict:
        headers.pop('upgrade-insecure-requests', None)
        headers.pop('sec-fetch-user', None)

        headers.update({
            'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
            'priority': 'u=2, i',
            'sec-fetch-dest': 'image',
            'sec-fetch-mode': 'no-cors',
            'sec-fetch-site': 'same-origin'
        })

        return Util.sort_dict_order(headers)

    @staticmethod
    def set_api_request_headers(headers: dict) -> dict:
        headers.pop('upgrade-insecure-requests', None)
        headers.pop('sec-fetch-user', None)

        headers.update({
            'accept': 'application/json, text/plain, */*',
            'priority': 'u=1, i',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site'
        })

        return Util.sort_dict_order(headers)