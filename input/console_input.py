from threading import Thread
from typing import Callable

from input.input import Input


class ConsoleInput(Input):
    def __init__(self):
        super().__init__()
        self._handler = None
        self._running = True
        self._event_thread = Thread(daemon=True, target=self._event_loop)

    def init(self):
        self._event_thread.start()

    def clear(self):
        self._running = False
        self._event_thread.join(timeout=2)

    def register_key_handler(self, handler: Callable[[], None]) -> None:
        self._handler = handler

    def _event_loop(self):
        while self._running:
            _ = input()
            if self._handler:
                self._handler()
