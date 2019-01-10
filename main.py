from client.config import ClientConfig
from client.resource import Resource
from config import SERVER_URL, RESOURCE_TYPE
from display.display import Display


def main() -> None:
    print('--- Ping Pong Pi Client starting... ---')
    print('> Server URL:    %s' % SERVER_URL)
    print('> Resource Type: %s' % RESOURCE_TYPE)
    print()

    config = ClientConfig(SERVER_URL)
    resource = Resource(RESOURCE_TYPE, config)
    display = Display.get_display()

    display.show_message('Hello! :)')


if __name__ == '__main__':
    main()
