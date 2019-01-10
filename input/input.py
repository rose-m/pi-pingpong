from abc import ABC, abstractmethod
from typing import Callable


class Input(ABC):
    _input = None

    @staticmethod
    def get_input() -> 'Input':
        if Input._input is None:
            Input._input = Input._initialize_input()
        return Input._input

    @staticmethod
    def _initialize_input() -> 'Input':
        sense_available = False
        try:
            import sense_hat
            sense_available = True
        except ImportError:
            print('Input: SenseHat not available - using console...')
            pass

        if sense_available:
            from input.sense_input import SenseInput
            input = SenseInput()
        else:
            from input.console_input import ConsoleInput
            input = ConsoleInput()

        input.init()
        return input

    def init(self):
        pass

    @abstractmethod
    def register_key_handler(self, handler: Callable[[], None]) -> None:
        pass
