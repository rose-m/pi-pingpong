from enum import Enum

from .config import ClientConfig


class ResourceStatus(Enum):
    FREE = 'free'
    RESERVED = 'reserved'
    OCCUPIED = 'occupied'


class Resource:
    API_PATH_OCCUPY = '/collab-resource/<resource>/occupy'
    API_PATH_FREE = '/collab-resource/<resource>/free'

    def __init__(self, resource_type: str, config: ClientConfig):
        self._type = resource_type
        self._config = config
        self._status = ResourceStatus.FREE

    def get_type(self) -> str:
        return self._type

    def get_status(self) -> ResourceStatus:
        return self._status

    def occupy(self) -> bool:
        # url = self._config.get_url(Resource.API_PATH_OCCUPY.replace('<resource>', self._type))
        return True

    def free(self) -> bool:
        # result = self._execute_request(Resource.API_PATH_OCCUPY.replace('<resource>', self._type))
        return True

    def start_periodic_checks(self) -> None:
        pass

    def stop_periodic_checks(self) -> None:
        pass
