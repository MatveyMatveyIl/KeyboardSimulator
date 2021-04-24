import sys
import EXCEPTIONS

try:
    from PyQt5.QtCore import QTimer
except Exception as e:
    print('PyQt5 not found: "{}".'.format(e))
    sys.exit(EXCEPTIONS.ERROR_QT_VERSION)


class StopWatch:
    '''секундомер'''
    def __init__(self):
        super().__init__()
        self.time = 0
        self.timer = QTimer()
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.tick)
        self.in_progress = False

    def tick(self):
        self.time += 1 / 100

    def do_start(self):
        if not self.in_progress:
            self.timer.start(10)
            self.in_progress = True

    def do_pause(self):
        self.in_progress = False
        self.timer.stop()

    def do_finish(self):
        self.timer.stop()
        self.time = 0
        self.in_progress = False


def seconds_to_minutes(time):
    time = time.split(':')
    min, sec = time[0], time[1]
    return float(min) + float(sec) / 60
