from PyQt5.QtCore import QTimer

class StopWatch():
    def __init__(self):
        super().__init__()
        self.time = 0
        self.timer = QTimer()
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.tick)
        self.in_progress = False


    def tick(self):
        self.time += 1/100

    def do_start(self):
        if not self.in_progress:
            self.timer.start(10)
            self.in_progress = True

    def do_pause(self):
        self.timer.stop()
        self.time = 0
        self.in_progress = False

