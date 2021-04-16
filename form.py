import dictionary
import sys
import EXCEPTIONS
import form_style
import statistic
from timer import *

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, \
        QLineEdit, QLabel, QComboBox, QMenuBar, QMenu, QAction
    from PyQt5.QtGui import QIcon, QTextCharFormat, QFont, QSyntaxHighlighter
    from PyQt5.QtCore import QTimer, pyqtSlot
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
        self.set_window_interface()
        self.set_user_text_box_interface()
        self.set_text_to_write_interface()
        self.set_level_box_interface()
        self.set_stopwatch_interface()
        self.set_menubar_interface()

    def set_window_interface(self):
        self.setWindowTitle('Keyboard simulator')
        self.setFixedSize(1028, 731)
        self.setWindowIcon(QIcon('pictures/programmIcon.png'))

    def set_user_text_box_interface(self):
        self.user_text_box = QLineEdit(self)
        self.user_text_box.setGeometry(50, 360, 701, 291)
        self.user_text_box.returnPressed.connect(self.on_click_enter)
        self.user_text_box.textChanged.connect(self.check_errors)
        self.user_text_box.textChanged.connect(self.update_time)

    def set_text_to_write_interface(self):
        self.text_to_write = QLabel(self)
        self.text_to_write.setGeometry(60, 90, 661, 181)
        self.text_to_write.setText(next(self.level_text))

    def set_level_box_interface(self):
        self.level_box = QComboBox(self)
        self.level_box.setGeometry(780, 100, 200, 60)
        self.level_box.addItem("Уровень 1 - Слова")
        self.level_box.addItem("Уровень 2 - Предложения")
        self.level_box.addItem("Уровень 3 - Текст")
        # self.level_box.activated.connect(self.set_color)

    def set_stopwatch_interface(self):
        self.timer_label = QLabel(self)
        self.timer_label.setText('0:00.00')
        self.timer_label.setGeometry(790, 360, 171, 81)

    def set_menubar_interface(self):
        self.statusBar()
        menubar = self.menuBar()
        menubar.setGeometry(0, 0, 1028, 26)
        menu = menubar.addMenu('Меню')
        stats = menubar.addMenu('Статистика')
        help = menubar.addMenu('Помощь')
        # self.stat1 = QAction("&По уровням", self)
        self.stat2 = QAction("Лучший результат", self)
        # stats.addAction(self.stat1)
        stats.addAction(self.stat2)
        levels = stats.addMenu("По уровням")
        levels.addAction("Слова")
        levels.addAction("Предложения")
        levels.addAction("Текст")

    @pyqtSlot()
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

    @pyqtSlot()
    def check_errors(self):
        self._errors = list(i for (i, (a, b)) in
                            enumerate(zip(self.text_to_write.text(),
                                          self.user_text_box.text()))
                            if a != b)
        #print(self._errors)

    @pyqtSlot()
    def update_time(self):
        self.stop_watch.do_start()
        self.stop_watch.timer.timeout.connect(self.print_time)

    @pyqtSlot()
    def print_time(self):
        self.timer_label.setText(
            "%d:%05.2f" % (self.stop_watch.time // 60,
                           self.stop_watch.time % 60))

    @pyqtSlot()
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
