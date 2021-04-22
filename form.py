import create_user_dict

try:
    import dictionary
    import sys
    import EXCEPTIONS
    import form_style
    import statistic
    from stopwatch import *
    from create_user_dict import *

except Exception as e:
    print('Modules not found: "{}". Try reinstalling the app.'.format(e))
    sys.exit(4)

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, \
        QLineEdit, QLabel, QComboBox, QMenuBar, QMenu, QAction, QTextEdit, QPlainTextEdit, QWidget, QPushButton
    from PyQt5.QtGui import QIcon, QTextCharFormat, QFont, QSyntaxHighlighter, QColor, QBrush
    from PyQt5.QtCore import QTimer, pyqtSlot, QEvent, QRegularExpression, Qt, QRegExp
    import pyqtgraph as pg
except Exception as e:
    print('PyQt5 not found: "{}".'.format(e))
    sys.exit(EXCEPTIONS.ERROR_QT_VERSION)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Keyboard simulator')
        self.setFixedSize(380, 449)
        self.setWindowIcon(QIcon('pictures/programmIcon.png'))
        self.helper = QPushButton(self)
        self.helper.setGeometry(50, 20, 261, 51)
        self.helper.setText("Помощь")
        self.user = QPushButton(self)
        self.user.setGeometry(50, 100, 261, 51)
        self.user.setText("Пользователь")
        self.add_text = QPushButton(self)
        self.add_text.setGeometry(50, 180, 261, 51)
        self.add_text.setText("Добавить текст")
        self.stat = QPushButton(self)
        self.stat.setGeometry(50, 270, 261, 51)
        self.stat.setText("Статистика")
        self.button = QPushButton(self)
        self.button.setGeometry(50, 350, 261, 51)
        self.button.setText("Начать")

    def show_main_window(self):
        self.w1 = MainWindow()
        self.w1.button.clicked.connect(self.show_window_keyboard)
        self.w1.button.clicked.connect(self.w1.close)
        self.w1.user.clicked.connect(self.show_user_interface)
        self.w1.user.clicked.connect(self.w1.close)
        self.w1.add_text.clicked.connect(self.show_add_text)
        self.w1.add_text.clicked.connect(self.w1.close)
        #self.w1.stat.clicked.connect(self.show_stat)
        self.w1.show()

    def show_window_keyboard(self):
        self.w2 = WindowKeyboardTrainer()
        self.w2.show()

    def show_user_interface(self):
        self.w3 = UserWindow()
        self.w3.show()

    def show_add_text(self):
        self.w4 = AddTextWindow()
        self.w4.show()

    # def show_stat(self):
    #     self.st1 = Stat()
    #     self.st1.showed()


class UserWindow(QWidget):
    def __init__(self):
        super(UserWindow, self).__init__()
        self.setWindowTitle('Keyboard simulator')
        self.setFixedSize(330, 390)
        self.setWindowIcon(QIcon('pictures/programmIcon.png'))
        self.login = QTextEdit(self)
        self.login.setGeometry(30, 20, 261, 51)
        self.add = QPushButton(self)
        self.add.setGeometry(30, 90, 261, 51)
        self.add.setText("Войти")
        self.save = QPushButton(self)
        self.save.setGeometry(30, 140, 261, 51)
        self.save.setText("Создать")
        self.add.clicked.connect(self.func2)
        self.add.clicked.connect(self.close)
        self.save.clicked.connect(self.func2)
        self.save.clicked.connect(self.close)

    def func2(self):
        self.w = MainWindow()
        self.w.show()
        self.w.show_main_window()
        self.w.close()


class AddTextWindow(QWidget):
    def __init__(self):
        super(AddTextWindow, self).__init__()
        self.setWindowTitle('Keyboard simulator')
        self.setFixedSize(967, 497)
        self.setWindowIcon(QIcon('pictures/programmIcon.png'))
        self.topic = QTextEdit(self)
        self.topic.setGeometry(300, 30, 331, 51)
        self.text = QTextEdit(self)
        self.text.setGeometry(40, 130, 871, 251)
        self.word = QPushButton(self)
        self.word.setGeometry(100, 410, 181, 41)
        self.word.setText("Слова")
        self.sentences = QPushButton(self)
        self.sentences.setGeometry(390, 410, 181, 41)
        self.sentences.setText("Предложения")
        self.label = QPushButton(self)
        self.label.setGeometry(670, 410, 181, 41)
        self.label.setText("Текст")
        self.word.clicked.connect(self.open_mainWindow)
        self.word.clicked.connect(self.add_words)
        self.word.clicked.connect(self.close)
        self.sentences.clicked.connect(self.open_mainWindow)
        self.sentences.clicked.connect(self.add_sentences)
        self.sentences.clicked.connect(self.close)
        self.label.clicked.connect(self.open_mainWindow)
        self.label.clicked.connect(self.add_text)
        self.label.clicked.connect(self.close)

    def open_mainWindow(self):
        create_words(self.text.toPlainText(), self.topic.toPlainText())
        self.w = MainWindow()
        self.w.show()
        self.w.show_main_window()
        self.w.close()

    def add_words(self):
        create_words(self.text.toPlainText(), self.topic.toPlainText())

    def add_sentences(self):
        create_sentences(self.text.toPlainText(), self.topic.toPlainText())

    def add_text(self):
        create_text(self.text.toPlainText(), self.topic.toPlainText())


class WindowKeyboardTrainer(QMainWindow):
    def __init__(self):
        super(WindowKeyboardTrainer, self).__init__()
        self.level_text = iter(dictionary.sentences['текст'])
        self.set_user_interface()
        self.stat = statistic.Statistic()
        self.stopwatch = StopWatch()
        self.symbols_state = []

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
        self.user_text_box = QTextEdit(self)
        self.user_text_box.setGeometry(60, 410, 661, 181)
        self.user_text_box.installEventFilter(self)
        self.user_text_box.textChanged.connect(self.check_errors)
        self.user_text_box.textChanged.connect(self.update_time)

    def set_text_to_write_interface(self):
        self.text_to_write = QTextEdit(self)
        self.text_to_write.setGeometry(60, 120, 661, 181)
        self.text_to_write.setReadOnly(True)
        self.text_to_write.setAcceptDrops(False)
        self.text_to_write.wordWrapMode()
        self.text_to_write.setText(next(self.level_text))

    def set_level_box_interface(self):
        self.level_box = QComboBox(self)
        self.level_box.setGeometry(780, 120, 200, 60)
        for topic in dictionary.sentences.keys():
            self.level_box.addItem(topic)

    def set_stopwatch_interface(self):
        self.timer_label = QLabel(self)
        self.timer_label.setText('0:00.00')
        self.timer_label.setGeometry(340, 320, 171, 81)
        self.start = QPushButton(self)
        self.start.setGeometry(100, 320, 190, 71)
        self.start.setText("Старт")
        self.finish = QPushButton(self)
        self.finish.setGeometry(440, 320, 190, 71)
        self.finish.setText("Конец")
        self.time = QLabel(self)
        self.time.setText("Время сеанса:")
        self.time.setGeometry(790, 300, 120, 52)
        self.time1 = QLabel(self)
        self.time1.setGeometry(890, 300, 120, 52)
        self.time1.setText("00:00:00")
        self.symb = QLabel(self)
        self.symb.setText("Символов в минуту:")
        self.symb.setGeometry(790, 340, 120, 52)
        self.symb1 = QLabel(self)
        self.symb1.setGeometry(920, 340, 120, 52)
        self.symb1.setText("00")

    # def show_window1(self):
    #     self.w = Window1()
    #     self.w.show()

    def set_menubar_interface(self):
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

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and obj is self.user_text_box:
            if event.key() == Qt.Key_Return and self.user_text_box.hasFocus():
                if self.user_text_box.toPlainText() == self.text_to_write.toPlainText():
                    self.equal_strings()
                    return True
        return False

    def equal_strings(self):
        self.user_text_box.clear()
        self.stopwatch.do_finish()
        self.stat.process_data(
            self.timer_label.text(),
            self.text_to_write.toPlainText())
        self.symbols_state = []
        self.timer_label.setText('0:00.00')
        try:
            self.text_to_write.setText(next(self.level_text))
        except StopIteration:
            pass  # message

    @pyqtSlot()
    def check_errors(self):
        state_list = []
        if len(self.text_to_write.toPlainText()) >= len(self.user_text_box.toPlainText()):
            for position in range(len(self.user_text_box.toPlainText())):
                if self.user_text_box.toPlainText()[position] == self.text_to_write.toPlainText()[position]:
                    state_list.append(('correct', position))
                else:
                    state_list.append(('wrong', position))
        self.set_color(state_list)

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
    def set_color(self, state_list):
        """Brush symbols"""
        cursor = self.text_to_write.textCursor()
        format = QTextCharFormat()
        for char_text in range(len(state_list)):
            if state_list[char_text][0] == 'correct':
                cursor.setPosition(state_list[char_text][1])
                cursor.movePosition(cursor.Right, 100)
                format.setBackground(QBrush(QColor('#a6f5c8')))
                cursor.mergeCharFormat(format)
            elif state_list[char_text][0] == 'wrong':
                cursor.setPosition(state_list[char_text][1])
                cursor.movePosition(cursor.Right, 100)
                format.setBackground(QBrush(QColor('#ff6e6e')))
                cursor.mergeCharFormat(format)
        if len(state_list) <= len(self.symbols_state):
            for white in range(0, len(self.symbols_state)):
                if white >= len(state_list):
                    cursor.setPosition(self.symbols_state[white][1])
                    cursor.movePosition(cursor.Right, 100)
                    brush = QBrush(QColor('white'))
                    format.setBackground(brush)
                    cursor.mergeCharFormat(format)
        self.symbols_state = state_list

    @pyqtSlot()
    def change_dictionary(self):
        pass


app = QApplication(sys.argv)
# app.setStyleSheet(form_style.style)
window = MainWindow()
window.show()
window.close()
window.show_main_window()
sys.exit(app.exec_())
# app.setStyleSheet(form_style.style)
