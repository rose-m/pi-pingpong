from sense_hat import SenseHat

from display.color import Color
from display.display import Display


class SenseDisplay(Display):
    SCROLL_SPEED = 1.0

    def __init__(self):
        super().__init__()
        self._sense = None

    def init(self):
        self._sense = SenseHat()

    def clear(self):
        self._sense.clear()

    def show_message(self, message: str, color: Color = Color.DEFAULT) -> None:
        self._sense.show_message(message, SenseDisplay.SCROLL_SPEED, self._convert_color(color))

    def show_timer(self, seconds_remaining: int, message: str = None, color: Color = Color.DEFAULT) -> None:
        self.show_message(
            '%s - %02d:%02d' % (message, seconds_remaining // 60, seconds_remaining % 60),
            color
        )

    @staticmethod
    def _convert_color(color: Color) -> [int, int, int]:
        if color is Color.RED:
            return [255, 0, 0]
        elif color is Color.GREEN:
            return [0, 255, 0]
        elif color is Color.YELLOW:
            return [255, 255, 0]
        return [255, 255, 255]
