try:
    from modules.dictionary import sentences
    import sys
    import random
    from modules import EXCEPTIONS, statistic
    from modules import form_style
    from modules.stopwatch import *
    from modules.create_user_dict import *

except Exception as e:
    print('Modules not found: "{}". Try reinstalling the app.'.format(e))
    sys.exit(4)

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, \
        QLineEdit, QLabel, QComboBox, QMenuBar, QMenu, QAction, QTextEdit, QPlainTextEdit, QWidget, QPushButton, \
        QMessageBox
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
        self.setWindowIcon(QIcon('pictures/ammIcon.png'))
        self.helper = QPushButton(self)
        self.helper.setGeometry(50, 30, 261, 51)
        self.helper.setText("Помощь")
        self.user = QPushButton(self)
        self.user.setGeometry(50, 110, 261, 51)
        self.user.setText("Пользователь")
        self.add_text = QPushButton(self)
        self.add_text.setGeometry(50, 190, 261, 51)
        self.add_text.setText("Добавить текст")
        self.stat = QPushButton(self)
        self.stat.setGeometry(50, 270, 261, 51)
        self.stat.setText("Статистика")
        self.button = QPushButton(self)
        self.button.setGeometry(50, 350, 261, 51)
        self.button.setText("Начать")

    def show_main_window(self):
        self.main_window = MainWindow()
        self.main_window.button.clicked.connect(self.show_window_keyboard)
        self.main_window.button.clicked.connect(self.main_window.close)
        self.main_window.user.clicked.connect(self.show_user_interface)
        self.main_window.user.clicked.connect(self.main_window.close)
        self.main_window.add_text.clicked.connect(self.show_add_text)
        self.main_window.add_text.clicked.connect(self.main_window.close)
        # self.main_window.stat.clicked.connect(self.show_stat)
        self.main_window.show()

    def show_window_keyboard(self):
        self.window_trainer = WindowKeyboardTrainer()
        self.window_trainer.show()

    def show_user_interface(self):
        self.user_window = UserWindow()
        self.user_window.show()

    def show_add_text(self):
        self.dict_window = AddTextWindow()
        self.dict_window.show()


class UserWindow(QWidget):
    def __init__(self):
        super(UserWindow, self).__init__()
        self.setWindowTitle('Keyboard simulator')
        self.setFixedSize(330, 390)
        self.setWindowIcon(QIcon('pictures/programmIcon.png'))
        self.login = QTextEdit(self)
        self.login.setGeometry(30, 20, 261, 51)
        self.login.setPlaceholderText("Введите имя")
        self.add = QPushButton(self)
        self.add.setGeometry(30, 90, 261, 51)
        self.add.setText("Войти")
        self.save = QPushButton(self)
        self.save.setGeometry(30, 140, 261, 51)
        self.save.setText("Создать")
        self.exit = QPushButton(self)
        self.exit.setGeometry(30, 300, 261, 51)
        self.exit.setText("Назад")
        self.exit.clicked.connect(self.show_main_window)
        self.exit.clicked.connect(self.close)

    def show_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.main_window.show_main_window()
        self.main_window.close()


class AddTextWindow(QWidget):
    def __init__(self):
        super(AddTextWindow, self).__init__()
        self.setWindowTitle('Keyboard simulator')
        self.setFixedSize(967, 465)
        self.setWindowIcon(QIcon('pictures/programmIcon.png'))
        self.topic = QTextEdit(self)
        self.topic.setGeometry(305, 30, 331, 51)
        self.topic.setPlaceholderText("Введите название")
        self.text = QTextEdit(self)
        self.text.setGeometry(45, 130, 871, 251)
        self.text.setPlaceholderText(
            "Вставьте текст. Слова должны состоять как минимум из 3 символов, предложения из 10")
        self.word = QPushButton(self)
        self.word.setGeometry(80, 410, 150, 41)
        self.word.setText("Слова")
        self.sentences = QPushButton(self)
        self.sentences.setGeometry(280, 410, 150, 41)
        self.sentences.setText("Предложения")
        self.label = QPushButton(self)
        self.label.setGeometry(480, 410, 150, 41)
        self.label.setText("Текст")
        self.close_btn = QPushButton(self)
        self.close_btn.setGeometry(680, 410, 150, 41)
        self.close_btn.setText('Назад')
        self.word.clicked.connect(self.add_words)
        self.sentences.clicked.connect(self.add_sentences)
        self.label.clicked.connect(self.add_text)
        self.close_btn.clicked.connect(self.open_mainWindow)
        self.close_btn.clicked.connect(self.close)

    def open_mainWindow(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.main_window.show_main_window()
        self.main_window.close()

    def add_words(self):
        create_words(self.text.toPlainText(), self.topic.toPlainText())
        self.critical_text()

    def add_sentences(self):
        create_sentences(self.text.toPlainText(), self.topic.toPlainText())
        self.critical_text()

    def add_text(self):
        create_text(self.text.toPlainText(), self.topic.toPlainText())
        self.critical_text()

    def critical_text(self):
        if len(self.text.toPlainText()) == 0:
            QMessageBox.critical(self, "Ошибка", "Вы не ввели текст", QMessageBox.Ok)
        elif len(self.topic.toPlainText()) == 0:
            QMessageBox.critical(self, "Ошибка", "Введите название", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Успешно", "Словарь создан", QMessageBox.Ok)


class WindowKeyboardTrainer(QMainWindow):
    def __init__(self):
        super(WindowKeyboardTrainer, self).__init__()
        self.set_user_interface()
        self.stat = statistic.Statistic()
        self.full_stopwatch = StopWatch()
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
        self.user_text_box.setGeometry(50, 410, 690, 270)
        self.user_text_box.setPlaceholderText("Выберите словарь, нажмите старт и начните ввод")
        self.user_text_box.installEventFilter(self)
        self.user_text_box.textChanged.connect(self.check_errors)
        #self.user_text_box.textChanged.connect(self.update_statistic)
        self.user_text_box.setReadOnly(True)

    def set_text_to_write_interface(self):
        self.text_to_write = QTextEdit(self)
        self.text_to_write.setGeometry(50, 30, 690, 270)
        self.text_to_write.setReadOnly(True)
        self.text_to_write.setAcceptDrops(False)
        self.text_to_write.wordWrapMode()

    def set_level_box_interface(self):
        self.level_box = QComboBox(self)
        self.level_box.setGeometry(780, 120, 200, 60)
        for topic in dictionary.sentences.keys():
            self.level_box.addItem(topic)

    def set_stopwatch_interface(self):
        self.stopwatch = StopWatch()
        self.timer_label = QLabel(self)
        self.timer_label.setText('0:00.00')
        self.timer_label.setGeometry(330, 335, 75, 41)
        self.start = QPushButton(self)
        self.start.setGeometry(100, 320, 190, 71)
        self.start.setText("Старт")
        self.start.clicked.connect(self.start_session)
        self.finish = QPushButton(self)
        self.finish.setGeometry(440, 320, 190, 71)
        self.finish.setText("Завершить")
        self.finish.clicked.connect(self.end_session)
        self.full_time_label = QLabel(self)
        self.full_time_label.setText("Время сеанса:")
        self.full_time_label.setGeometry(750, 300, 150, 41)
        self.full_time_value = QLabel(self)
        self.full_time_value.setGeometry(890, 300, 90, 41)
        self.full_time_value.setText("00:00:00")
        self.CPM = QLabel(self)
        self.CPM.setText("CPM:")
        self.CPM.setGeometry(750, 340, 150, 41)
        self.CPM_value = QLabel(self)
        self.CPM_value.setGeometry(890, 340, 90, 41)
        self.CPM_value.setText("00")
        self.WPM = QLabel(self)
        self.WPM.setGeometry(750, 380, 150, 41)
        self.WPM.setText("WPM:")
        self.WPM_value = QLabel(self)
        self.WPM_value.setGeometry(890, 380, 90, 41)
        self.WPM_value.setText("00")

    def start_session(self):
        """Session start/pause handling"""
        if self.start.text() in {'Старт', 'Продолжить'}:
            self.user_text_box.setReadOnly(False)
            self.level_box.setDisabled(True)
            if self.full_time_value != '0:00.00' and len(self.user_text_box.toPlainText()) != 0:
                self.stopwatch.do_start()
                self.full_stopwatch.do_start()
            if len(self.text_to_write.toPlainText()) == 0:
                self.text_to_write.setText(random.choice(sentences[self.level_box.currentText()]))
            self.user_text_box.textChanged.connect(self.update_time)
            self.start.setText('Пауза')
        else:
            self.user_text_box.setReadOnly(True)
            self.level_box.setDisabled(False)
            self.start.setText('Продолжить')
            self.stopwatch.do_pause()
            self.full_stopwatch.do_pause()

    def end_session(self):
        """End session handling"""
        self.level_box.setDisabled(False)
        self.user_text_box.setReadOnly(True)
        self.user_text_box.clear()
        self.text_to_write.setText('')
        self.stopwatch.do_finish()
        self.timer_label.setText('0:00.00')
        self.full_time_value.setText('0:00.00')
        self.full_stopwatch.time = 0
        self.start.setText('Старт')

    def set_menubar_interface(self):
        self.menu = QPushButton(self)
        self.menu.setGeometry(760, 610, 221, 41)
        self.menu.setText("Выход в меню")
        self.menu.clicked.connect(self.switch_window)
        self.menu.clicked.connect(self.close)

    def switch_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.main_window.show_main_window()
        self.main_window.close()

    def eventFilter(self, obj, event):
        """Check input if pressed key is Enter"""
        if event.type() == QEvent.KeyPress and obj is self.user_text_box:
            if event.key() == Qt.Key_Return and self.user_text_box.hasFocus():
                if self.user_text_box.toPlainText() == self.text_to_write.toPlainText():
                    self.equal_strings()
                    return True
        return False

    def equal_strings(self):
        self.user_text_box.clear()
        self.stopwatch.do_finish()
        self.full_stopwatch.do_pause()
        # self.stat.process_data(
        #     self.timer_label.text(),
        #     self.text_to_write.toPlainText())
        self.symbols_state = []
        self.timer_label.setText('0:00.00')
        try:
            self.text_to_write.setText(random.choice(sentences[self.level_box.currentText()]))
        except StopIteration:
            QMessageBox.information(self, "Вы закончили", 'поздравляем', QMessageBox.Ok)

    @pyqtSlot()
    def check_errors(self):
        """Checks the entered text and compares errors with the original"""
        state_list = []
        if len(self.text_to_write.toPlainText()) >= len(self.user_text_box.toPlainText()):
            for position in range(len(self.user_text_box.toPlainText())):
                if self.user_text_box.toPlainText()[position] == self.text_to_write.toPlainText()[position]:
                    state_list.append(('correct', position))
                else:
                    state_list.append(('wrong', position))
        self.set_color(state_list)
        self.stat.process_data(self.full_time_value.text(), ' ',
                               len(list(filter(lambda x: x[0] == 'wrong', self.symbols_state))))

    @pyqtSlot()
    def update_time(self):
        """Stopwatch update"""
        self.stopwatch.do_start()
        self.full_stopwatch.do_start()
        self.stopwatch.timer.timeout.connect(self.print_time)
        self.full_stopwatch.timer.timeout.connect(self.update_statistic)


    @pyqtSlot()
    def print_time(self):
        self.timer_label.setText(
            "%d:%05.2f" % (self.stopwatch.time // 60,
                           self.stopwatch.time % 60))
        self.full_time_value.setText(
            "%d:%05.2f" % (self.full_stopwatch.time // 60,
                           self.full_stopwatch.time % 60))

    @pyqtSlot()
    def update_statistic(self):
        self.CPM_value.setText(str(self.stat.statistic['CPM'].value) + 'сим/мин')

    @pyqtSlot()
    def set_color(self, state_list):
        """highlights valid and invalid characters"""
        cursor = self.text_to_write.textCursor()
        format = QTextCharFormat()
        if len(self.user_text_box.toPlainText()) <= len(self.text_to_write.toPlainText()):
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
                        brush = QBrush(QColor('#E6E6FA'))
                        format.setBackground(brush)
                        cursor.mergeCharFormat(format)
            self.symbols_state = state_list
