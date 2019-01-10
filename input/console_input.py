from threading import Thread
from typing import Callable

from input.input import Input


class ConsoleInput(Input):
    def __init__(self):
        super().__init__()
        self._handler = None
        self._event_thread = Thread(daemon=True, target=self._event_loop)

    def init(self):
        self._event_thread.start()

    def register_key_handler(self, handler: Callable[[], None]) -> None:
        self._handler = handler

    def _event_loop(self):
        while True:
            _ = input()
            if self._handler:
                self._handler()
