from threading import Thread
from time import sleep

from display.color import Color
from display.display import Display
from shared.sense_hat import Sense


class SenseDisplay(Display):
    SCROLL_SPEED = 0.06

    def __init__(self):
        super().__init__()
        self._message = None
        self._color = None
        self._thread = None
        self._running = True

    def init(self) -> None:
        self._thread = Thread(target=self._render_message)
        self._thread.start()

    def clear(self) -> None:
        self._running = False
        self._thread.join(timeout=2)
        Sense.hat().clear()

    def show_message(self, message: str, color: Color = Color.DEFAULT) -> None:
        self._message = message
        self._color = color

    def show_timer(self, seconds_remaining: int, message: str = None, color: Color = Color.DEFAULT) -> None:
        self.show_message(
            '%s - %02d:%02d' % (message, seconds_remaining // 60, seconds_remaining % 60),
            color
        )

    def _render_message(self) -> None:
        while self._running:
            if self._message is not None:
                Sense.hat().show_message(self._message, SenseDisplay.SCROLL_SPEED, self._convert_color(self._color))
            sleep(0.5)

    @staticmethod
    def _convert_color(color: Color) -> [int, int, int]:
        if color is Color.RED:
            return [255, 0, 0]
        elif color is Color.GREEN:
            return [0, 255, 0]
        elif color is Color.YELLOW:
            return [255, 255, 0]
        return [255, 255, 255]
