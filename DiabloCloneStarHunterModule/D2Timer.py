import math
import time

from PyQt5 import QtTest


def sleep(millisecond, func=None):
    per = 200
    s = time.time() * 1000
    count = math.ceil(millisecond / per)
    for i in range(count):
        e = time.time() * 1000 - s
        if e > millisecond:
            if func:
                func(0)
            return

        remainMillisecond = millisecond - e
        if func:
            if remainMillisecond >= 0:
                func(remainMillisecond)
            else:
                func(0)

        if remainMillisecond >= 0:
            QtTest.QTest.qWait(per)
