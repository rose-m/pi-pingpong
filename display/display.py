from abc import ABC, abstractmethod

from display.color import Color


class Display(ABC):
    _display = None

    @staticmethod
    def get_display() -> 'Display':
        if Display._display is None:
            Display._display = Display._initialize_display()
        return Display._display

    @staticmethod
    def _initialize_display() -> 'Display':
        sense_available = False
        try:
            import sense_hat
            sense_available = True
        except ImportError:
            print('SenseHat not available - using console...')
            pass

        if sense_available:
            from display.sense_display import SenseDisplay
            display = SenseDisplay()
        else:
            from display.console_display import ConsoleDisplay
            display = ConsoleDisplay()

        display.init()
        return display

    def init(self) -> None:
        pass

    def clear(self) -> None:
        pass

    @abstractmethod
    def show_message(self, message: str, color: Color = Color.DEFAULT) -> None:
        pass

    @abstractmethod
    def show_timer(self, seconds_remaining: int, message: str = None, color: Color = Color.DEFAULT) -> None:
        pass
