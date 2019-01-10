from threading import Thread
from time import sleep
from typing import Callable

from input.input import Input
from shared.sense_hat import Sense


class SenseInput(Input):
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
            events = Sense.hat().stick.get_events()
            if len(events) > 0 and self._handler is not None:
                self._handler()
            sleep(0.5)
