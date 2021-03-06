import atexit
from time import sleep

from client.config import ClientConfig
from client.resource import Resource, ResourceStatus
from config import SERVER_URL, RESOURCE_TYPE
from display.color import Color
from display.display import Display
from input.input import Input


def main() -> None:
    print('--- Ping Pong Pi Client starting... ---')
    print('> Server URL:    %s' % SERVER_URL)
    print('> Resource Type: %s' % RESOURCE_TYPE)
    print()

    config = ClientConfig(SERVER_URL)
    display = Display.get_display()
    input = Input.get_input()
    atexit.register(input.clear)
    atexit.register(display.clear)

    try:
        with Resource(RESOURCE_TYPE, config) as resource:
            input.register_key_handler(lambda: handle_input(resource))
            last_status = resource.get_status()
            display.show_message(last_status.name, get_color_for_status(last_status))
            while True:
                status = resource.get_status()
                if last_status != status:
                    print('Status changed to: %s' % status)
                    display.show_message(status.name, get_color_for_status(status))
                    last_status = status
                try:
                    sleep(1)
                except KeyboardInterrupt:
                    exit()
    except ConnectionError:
        display.show_message('Initial status check failed - stopping', Color.RED)


def handle_input(resource: Resource):
    status = resource.get_status()
    if status is ResourceStatus.RESERVED:
        resource.occupy()
    elif status is ResourceStatus.OCCUPIED:
        resource.release()
    elif status is ResourceStatus.FREE:
        resource.occupy()


def get_color_for_status(status: ResourceStatus) -> Color:
    if status is ResourceStatus.FREE:
        return Color.GREEN
    elif status is ResourceStatus.OCCUPIED:
        return Color.DEFAULT
    elif status is ResourceStatus.RESERVED:
        return Color.RED


if __name__ == '__main__':
    main()
