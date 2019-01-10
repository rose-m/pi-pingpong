from sense_hat import SenseHat


class Sense:
    _sense = None

    @staticmethod
    def hat() -> SenseHat:
        if Sense._sense is None:
            Sense._sense = SenseHat()
        return Sense._sense
