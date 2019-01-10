class ClientConfig:

    def __init__(self, base_url: str):
        if base_url.endswith('/'):
            base_url = base_url[0:-1]

        self._base_url = base_url

    def get_url(self, path: str) -> str:
        if not path.startswith('/'):
            path = '/' + path

        return self._base_url + path
