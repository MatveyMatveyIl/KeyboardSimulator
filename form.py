import dictionary
import sys
import EXCEPTIONS
import form_style
import statistic
from timer import *

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
    from PyQt5.QtGui import QIcon, QTextCharFormat, QFont, QSyntaxHighlighter
    from PyQt5.QtCore import QTimer
except Exception as e:
    print('PyQt5 not found: "{}".'.format(e))
    sys.exit(EXCEPTIONS.ERROR_QT_VERSION)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.level_text = iter(dictionary.sentences['easy'])
        self.set_user_interface()
        self._errors = []
        self.stat = statistic.Statistic()
        self.stop_watch = StopWatch()

    def set_user_interface(self):
        self.setWindowTitle('Keyboard simulator')
        self.setGeometry(500, 400, 600, 300)
        self.setWindowIcon(QIcon('pictures/programmIcon.png'))

        self.timer_label = QLabel(self)
        self.timer_label.setText('0:00.00')
        self.timer_label.setGeometry(400, 50, 100, 100)

        self.text_to_write = QLabel(self)
        self.text_to_write.setGeometry(50, 100, 500, 40)
        self.text_to_write.setText(next(self.level_text))

        self.user_text_box = QLineEdit(self)
        self.user_text_box.setGeometry(50, 200, 500, 40)
        self.user_text_box.returnPressed.connect(self.on_click_enter)
        self.user_text_box.textChanged.connect(self.check_errors)
        self.user_text_box.textChanged.connect(self.update_time)
        #self.user_text_box.textChanged.connect(self.set_color)#спросить

    def on_click_enter(self):
        if self.user_text_box.text() == self.text_to_write.text():
            self.user_text_box.setText('')
            self.stop_watch.do_pause()
            self.timer_label.setText('0:00.00')
            try:
                self.text_to_write.setText(next(self.level_text))
                print('correct')
            except StopIteration:
                print('wrong')
                pass #message

    def check_errors(self):
        self._errors = list(i for (i, (a, b)) in
                            enumerate(zip(self.text_to_write.text(),
                                          self.user_text_box.text()))
                            if a != b)
        #print(self._errors)

    def update_time(self):
        self.stop_watch.do_start()
        self.stop_watch.timer.timeout.connect(self.print_time)

    def print_time(self):
        self.timer_label.setText(
            "%d:%05.2f" % (self.stop_watch.time // 60, self.stop_watch.time % 60))

    def set_color(self):
        self.text_to_write.setStyleSheet('background-color: #a6f5c8;')
        if len(self._errors) == 0:
            pass
        self.text_to_write.setStyleSheet('background-color: #ff6e6e;')

# class SyntaxHighlighter(QSyntaxHighlighter):
#     def __init__(self, parrent):
#         super().__init__(parrent)
#
#     def color_line(self, line_num):
#         self.rehighlightBlock()


app = QApplication(sys.argv)
#app.setStyleSheet(form_style.style)
window = Window()
window.show()
sys.exit(app.exec_())