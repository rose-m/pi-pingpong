from abc import ABC, abstractmethod

from display.color import Color


class Display(ABC):
    _display: 'Display' = None

    @staticmethod
    def get_display() -> 'Display':
        if Display._display is None:
            Display._display = Display._initialize_display()
        return Display._display

    @staticmethod
    def _initialize_display() -> 'Display':
        from display.console_display import ConsoleDisplay
        display = ConsoleDisplay()
        display.init()
        return display

    def init(self) -> None:
        pass

    @abstractmethod
    def show_message(self, message: str, color: Color = Color.DEFAULT) -> None:
        pass

    @abstractmethod
    def show_timer(self, seconds_remaining: int, message: str = None, color: Color = Color.DEFAULT) -> None:
        pass
