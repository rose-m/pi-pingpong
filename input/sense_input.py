from threading import Thread
from typing import Callable

from input.input import Input
from shared.sense_hat import Sense


class SenseInput(Input):
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
            event = Sense.hat().stick.wait_for_event()
            if event is not None and self._handler is not None:
                self._handler()
