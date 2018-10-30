import serial

VALID_INPUT = ["1", "2", "3", "4", "5", "x", "a"]


class Cube(object):
    def __init__(self, port="/dev/ttyUSB0"):
        self.com = serial.Serial(port)
        self.com.write(b"x")  # turn everything off

    @staticmethod
    def _is_valid(s):
        return s in VALID_INPUT

    def write(self, s):
        if not self._is_valid(s):
            return False
        b = s.encode()
        self.com.write(b)
        return True


class CubeMock(Cube):
    def __init__(self, port=None):
        pass

    def write(self, s):
        if not self._is_valid(s):
            return False
        print(s)
        return True
