
MILLISECONDS_PER_DAY  =  86400000
FORMAT_MAX            = 100000000


def ms_to_notime(value:int) -> int:
    return round(float(value % MILLISECONDS_PER_DAY)
        * (float(FORMAT_MAX) / float(MILLISECONDS_PER_DAY))) % FORMAT_MAX

def notime_to_ms(value:int) -> int:
    return round(float(value % FORMAT_MAX)
        * (float(MILLISECONDS_PER_DAY) / float(FORMAT_MAX))) % MILLISECONDS_PER_DAY


class notime:

    def __init__(self, value:int):
        self.value = round(value) % FORMAT_MAX

    @classmethod
    def from_time(cls, hour:int, minute:int, second:int, millisecond:int):
        hour = round(hour) % 24
        minute = round(minute) % 60
        second = round(second) % 60
        millisecond = round(millisecond) % 1000
        sum_ = (hour * 60 * 60 * 1000)\
            + (minute * 60 * 1000)\
            + (second * 1000)\
            + millisecond
        return cls(ms_to_notime(sum_))

    def to_ms(self):
        return notime_to_ms(self.value)

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return str(self.value)

    def __int__(self):
        return self.value

    def __add__(self, value:int):
        return self.__class__(self.value + value)

    def __sub__(self, value:int):
        return self.__class__(self.value - value)

    def __mul__(self, value:int):
        return self.__class__(self.value * value)

    def __truediv__(self, value:float):
        return self.__class__(float(self.value) / float(value))

    def __pow__(self, value:int):
        return self.__class__(float(self.value) ** float(value))

    def __eq__(self, value:int):
        return self.value == value

    def __gt__(self, value:int):
        return self.value > value

    def __ge__(self, value:int):
        return self.value >= value

    def __lt__(self, value:int):
        return self.value < value

    def __le__(self, value:int):
        return self.value <= value
