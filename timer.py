import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton
from PyQt5.QtGui import QIcon, QTextCharFormat, QFont, QSyntaxHighlighter
from PyQt5.QtCore import QTimer

TICK_TIME = 1

class StopWatch(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(500, 400, 600, 300)
        self.timer = QTimer()
        self.timer.setInterval(TICK_TIME)
        self.timer.timeout.connect(self.tick)
        self.time_text = QLabel(self)
        self.time_text.setGeometry(100, 100, 100, 100)
        self.start = QPushButton(self)
        self.start.clicked.connect(self.do_start)

        self.do_reset()

    def display(self):
        self.time_text.setText("%d:%05.2f" % (self.time // 60, self.time % 60))

    def tick(self):
        self.time += TICK_TIME/100
        self.display()

    def do_start(self):
        self.timer.start(10)
        self.start.setText("Pause")
        self.start.clicked.disconnect()
        self.start.clicked.connect(self.do_pause)

    def do_pause(self):
        self.timer.stop()
        self.start.setText("Start")
        self.start.clicked.disconnect()
        self.start.clicked.connect(self.do_start)

    def do_reset(self):
        self.time = 0
        self.display()

app = QApplication(sys.argv)

watch = StopWatch()
watch.show()

sys.exit(app.exec_())