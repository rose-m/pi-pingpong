from enum import Enum
from threading import Timer

import requests

from .config import ClientConfig


class ResourceStatus(Enum):
    FREE = 'free'
    RESERVED = 'reserved'
    OCCUPIED = 'occupied'


class Resource:
    API_PATH_STATUS = '/collaboration-resource/<resource>/status'
    API_PATH_OCCUPY = '/collaboration-resource/<resource>/occupy'
    API_PATH_RELEASE = '/collaboration-resource/<resource>/release'

    def __init__(self, resource_type: str, config: ClientConfig):
        self._type = resource_type
        self._config = config
        self._status = ResourceStatus.FREE
        self._validity = -1

        self._poll_timer: Timer = None

    def __enter__(self) -> 'Resource':
        try:
            self._check_status()
            self._start_timer()
            return self
        except Exception:
            # just raise a ConnectionError for the initial check
            raise ConnectionError()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._clear_timer()

    def get_type(self) -> str:
        return self._type

    def get_status(self) -> ResourceStatus:
        return self._status

    def get_validity(self) -> int:
        return self._validity

    def occupy(self) -> bool:
        # url = self._config.get_url(Resource.API_PATH_OCCUPY.replace('<resource>', self._type))
        return True

    def free(self) -> bool:
        # result = self._execute_request(Resource.API_PATH_OCCUPY.replace('<resource>', self._type))
        return True

    def _check_status(self) -> None:
        url = self._config.get_url(Resource.API_PATH_STATUS.replace('<resource>', self.get_type()))
        res = requests.get(url, timeout=2).json()
        self._status = ResourceStatus[res['status']]
        if 'timeRemaining' in res:
            self._validity = res['timeRemaining']

    def _start_timer(self) -> None:
        self._clear_timer()
        self._poll_timer = Timer(5, self._run_timer)
        self._poll_timer.start()

    def _run_timer(self) -> None:
        try:
            self._check_status()
        except Exception:
            # we silently ignore and continue...
            pass
        self._start_timer()

    def _clear_timer(self) -> None:
        if self._poll_timer is not None:
            self._poll_timer.cancel()
            self._poll_timer = None
