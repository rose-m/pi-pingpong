import atexit
from time import sleep

from client.config import ClientConfig
from client.resource import Resource, ResourceStatus
from config import SERVER_URL, RESOURCE_TYPE
from display.color import Color
from display.display import Display


def main() -> None:
    print('--- Ping Pong Pi Client starting... ---')
    print('> Server URL:    %s' % SERVER_URL)
    print('> Resource Type: %s' % RESOURCE_TYPE)
    print()

    config = ClientConfig(SERVER_URL)
    display = Display.get_display()
    atexit.register(display.clear)

    try:
        with Resource(RESOURCE_TYPE, config) as resource:
            last_status = resource.get_status()
            display.show_message('Status: %s' % last_status.name, get_color_for_status(last_status))
            while True:
                status = resource.get_status()
                if last_status != status:
                    print('Status changed to: %s' % status)
                    display.show_message('Status: %s' % status.name, get_color_for_status(status))
                    last_status = status
                try:
                    sleep(1)
                except KeyboardInterrupt:
                    exit()
    except ConnectionError:
        display.show_message('Initial status check failed - stopping', Color.RED)


def get_color_for_status(status: ResourceStatus) -> Color:
    if status is ResourceStatus.FREE:
        return Color.GREEN
    elif status is ResourceStatus.OCCUPIED:
        return Color.DEFAULT
    elif status is ResourceStatus.RESERVED:
        return Color.RED


if __name__ == '__main__':
    main()
