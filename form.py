try:
    import dictionary
    import sys
    import EXCEPTIONS
    import form_style
    import statistic
    from stopwatch import *
except Exception as e:
    print('Modules not found: "{}". Try reinstalling the app.'.format(e))
    sys.exit(4)

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QLineEdit, QLabel, QComboBox, QMenuBar, QMenu, QAction, QTextEdit, QPlainTextEdit, QWidget, QPushButton
    from PyQt5.QtGui import QIcon, QTextCharFormat, QFont, QSyntaxHighlighter, QColor
    from PyQt5.QtCore import QTimer, pyqtSlot, QEvent, QRegularExpression, Qt, QRegExp
    import pyqtgraph as pg
    import numpy as np
except Exception as e:
    print('PyQt5 not found: "{}".'.format(e))
    sys.exit(EXCEPTIONS.ERROR_QT_VERSION)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Keyboard simulator')
        self.setFixedSize(380, 449)
        self.setWindowIcon(QIcon('pictures/programmIcon.png'))
        self.setting = QPushButton(self)
        self.setting.setGeometry(10, 110, 351, 51)
        self.setting.setText("Настройки")
        self.help = QPushButton(self)
        self.help.setGeometry(10, 40, 351, 51)
        self.help.setText("Помощь")
        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(10, 180, 351, 41)
        self.textEdit.setText("Введите имя пользователя")
        self.save = QPushButton(self)
        self.save.setGeometry(140, 220, 93, 28)
        self.save.setText("Сохранить")
        self.button = QPushButton(self)
        self.button.setGeometry(60, 360, 261, 41)
        self.button.setText("Продолжить")

    def show_main_window(self):
        self.w1 = MainWindow()
        self.w1.button.clicked.connect(self.show_window_keyboard)
        self.w1.button.clicked.connect(self.w1.close)
        self.w1.show()

    def show_window_keyboard(self):
        self.w2 = WindowKeyboardTrainer()
        self.w2.show()


class WindowKeyboardTrainer(QMainWindow):
    def __init__(self):
        super(WindowKeyboardTrainer, self).__init__()
        self.level_text = iter(dictionary.sentences['easy'])
        self.set_user_interface()
        self._errors = []
        self._mistakes = set()
        self.stat = statistic.Statistic()
        self.stopwatch = StopWatch()

    def set_user_interface(self):
        self.set_window_interface()
        self.set_user_text_box_interface()
        self.set_text_to_write_interface()
        self.set_level_box_interface()
        self.set_stopwatch_interface()
        self.set_menubar_interface()
        self.set_statistic_interface()

    def set_window_interface(self):
        self.setWindowTitle('Keyboard simulator')
        self.setFixedSize(1028, 731)
        self.setWindowIcon(QIcon('pictures/programmIcon.png'))

    def set_user_text_box_interface(self):
        self.user_text_box = QTextEdit(self)
        self.user_text_box.setGeometry(50, 360, 701, 291)
        self.user_text_box.installEventFilter(self)
        self.user_text_box.textChanged.connect(self.check_errors)
        self.user_text_box.textChanged.connect(self.update_time)

    def set_text_to_write_interface(self):
        self.text_to_write = QTextEdit(self)
        self.text_to_write.setGeometry(60, 90, 661, 181)
        self.text_to_write.setReadOnly(True)
        self.text_to_write.setAcceptDrops(False)
        self.text_to_write.wordWrapMode()
        self.text_to_write.setText(next(self.level_text))

    def set_level_box_interface(self):
        self.level_box = QComboBox(self)
        self.level_box.setGeometry(780, 100, 200, 60)
        self.level_box.addItem("Уровень 1 - Слова")
        self.level_box.addItem("Уровень 2 - Предложения")
        self.level_box.addItem("Уровень 3 - Текст")
        self.level_box.activated.connect(self.change_dictionary)

    def set_stopwatch_interface(self):
        self.timer_label = QLabel(self)
        self.timer_label.setText('0:00.00')
        self.timer_label.setGeometry(790, 360, 171, 81)

    def set_menubar_interface(self):
        self.statusBar()
        menubar = self.menuBar()
        menubar.setGeometry(0, 0, 1028, 26)
        # menu = menubar.addMenu('Меню')
        # menu.triggered.connect(self.func)
        stats = menubar.addMenu('Статистика')
        help = menubar.addMenu('Помощь')
        # self.stat1 = QAction("&По уровням", self)
        self.stat2 = QAction("Лучший результат", self)
        # stats.addAction(self.stat1)
        stats.addAction(self.stat2)
        levels = stats.addMenu("По уровням")
        levels.addAction("Слова")
        # levels.triggered.connect(self.func)
        levels.addAction("Предложения")
        levels.addAction("Текст")
        self.menu = QPushButton(self)
        self.menu.setGeometry(780, 610, 221, 41)
        self.menu.setText("Выход в меню")
        self.menu.clicked.connect(self.func)
        self.menu.clicked.connect(self.close)

    def func(self):
        self.w = MainWindow()
        self.w.show()
        self.w.show_main_window()
        self.w.close()

    def set_statistic_interface(self):
        self.btn = QPushButton(self)
        self.btn.setGeometry(780, 410, 221, 41)
        self.btn.setText("статистика")
        self.btn.clicked.connect(self.show_statistic)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and obj is self.user_text_box:
            if event.key() == Qt.Key_Return and self.user_text_box.hasFocus():
                if self.user_text_box.toPlainText() == self.text_to_write.toPlainText():
                    self.equal_strings()
                    return True
        return False

    def equal_strings(self):
        self.user_text_box.clear()
        self.stopwatch.do_pause()
        self.stat.process_data(
            self.timer_label.text(), {
                'errors_count': len(self._mistakes),
                'count_symbols': len(self.text_to_write.toPlainText()),
            },
            self.text_to_write.toPlainText())
        self._mistakes = set()
        self.timer_label.setText('0:00.00')
        try:
            self.text_to_write.setText(next(self.level_text))
        except StopIteration:
            pass  # message

    @pyqtSlot()
    def check_errors(self):
        self._errors = list(i for (i, (a, b)) in
                            enumerate(zip(self.text_to_write.toPlainText(),
                                          self.user_text_box.toPlainText()))
                            if a != b)
        self._mistakes = self._mistakes.union(set(self._errors))


    @pyqtSlot()
    def update_time(self):
        self.stopwatch.do_start()
        self.stopwatch.timer.timeout.connect(self.print_time)

    @pyqtSlot()
    def print_time(self):
        self.timer_label.setText(
            "%d:%05.2f" % (self.stopwatch.time // 60,
                           self.stopwatch.time % 60))

    @pyqtSlot()
    def set_color(self):
        self.text_to_write.setStyleSheet('background-color: #a6f5c8;')
        if len(self._errors) == 0:
            pass
        self.text_to_write.setStyleSheet('background-color: #ff6e6e;')

    @pyqtSlot()
    def change_dictionary(self):
        pass

    @pyqtSlot()
    def show_statistic(self):
        pass


app = QApplication(sys.argv)
# app.setStyleSheet(form_style.style)
window = MainWindow()
window.show()
window.close()
window.show_main_window()
sys.exit(app.exec_())
# app.setStyleSheet(form_style.style)
