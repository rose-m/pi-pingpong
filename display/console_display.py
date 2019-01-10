from display.color import Color
from display.display import Display


class ConsoleDisplay(Display):
    def show_message(self, message: str, color: Color = Color.DEFAULT) -> None:
        print(message)

    def show_timer(self, seconds_remaining: int, message: str = None, color: Color = Color.DEFAULT) -> None:
        print('Remaining: %02d:%02d' % (seconds_remaining // 60, seconds_remaining % 60))
