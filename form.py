try:
    from modules.dictionary import sentences
    import sys
    import random
    from modules import EXCEPTIONS, statistic
    from modules import form_style
    from modules.stopwatch import *
    from modules.create_user_dict import *
    import datetime
    from data import *
    import matplotlib.pyplot as plt
    import numpy as np
except Exception as e:
    print('Modules not found: "{}". Try reinstalling the app.'.format(e))
    sys.exit(4)

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, \
        QLineEdit, QLabel, QComboBox, QMenuBar, QMenu, QAction, QTextEdit, QPlainTextEdit, QWidget, QPushButton, \
        QMessageBox
    from PyQt5.QtGui import QIcon, QTextCharFormat, QFont, QSyntaxHighlighter, QColor, QBrush, QRegion
    from PyQt5.QtCore import QTimer, pyqtSlot, QEvent, QRegularExpression, Qt, QRegExp, QUrl, QDir
    from PyQt5.QtMultimedia import QMultimedia, QMediaPlayer, QMediaContent
except Exception as e:
    print('PyQt5 not found: "{}".'.format(e))
    sys.exit(EXCEPTIONS.ERROR_QT_VERSION)


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Keyboard simulator')
        self.setFixedSize(380, 450)
        self.setWindowIcon(QIcon('pictures/programmIcon.png'))
        buttons_name = ['Помощь', 'Пользователь', 'Статистика', 'Добавить текст', 'Старт']
        buttons = []
        for i, name in enumerate(buttons_name):
            button = QPushButton(self)
            button.setGeometry(50, 30 + 80 * i, 260, 50)
            button.setText(name)
            buttons.append(button)
        self.helper = buttons[0]
        self.user = buttons[1]
        self.stat = buttons[2]
        self.add_text = buttons[3]
        self.button_start = buttons[4]

    def show_main_window(self):
        windows = {'keyboard': WindowKeyboardTrainer(), 'add_text': AddTextWindow()}
        self.main_window = MainWindow()
        self.main_window.button_start.clicked.connect(lambda: self.show_window(windows['keyboard']))
        self.main_window.button_start.clicked.connect(self.main_window.close)
        self.main_window.add_text.clicked.connect(lambda: self.show_window(windows['add_text']))
        self.main_window.add_text.clicked.connect(self.main_window.close)
        self.main_window.stat.clicked.connect(self.stat1)
        self.main_window.show()


    def show_window(self, name):
        self.window = name
        self.window.show()

    def stat1(self):
        date = []
        wpm = []
        cpm = []
        errors = []
        for i in range(0, len(take_results())):
            date.append(take_results()[i][0])
            wpm.append(take_results()[i][1])
            cpm.append(take_results()[i][2])
            errors.append(take_results()[i][3])
        self.x = np.array(date)
        self.y = np.array(wpm)
        self.y1 = np.array(cpm)
        self.y2 = np.array(errors)
        plt.figure(figsize= (17, 7))
        man = plt.get_current_fig_manager()
        man.canvas.set_window_title("Статистика")
        plt.subplot(221)
        plt.plot(self.x, self.y, '-', marker="o", c="g")
        plt.title("Wpm")
        plt.grid()
        plt.subplot(222)
        plt.plot(self.x, self.y1, '-.',  marker="o", c="b")
        plt.title("Cpm")
        plt.grid()
        plt.subplot(223)
        plt.plot(self.x, self.y2, '--', marker="o", c="r")
        plt.title("Ошибки")
        plt.grid()
        plt.show()


class AddTextWindow(QWidget):
    def __init__(self):
        super(AddTextWindow, self).__init__()
        self.setWindowTitle('Keyboard simulator')
        self.setFixedSize(970, 465)
        self.setWindowIcon(QIcon('pictures/programmIcon.png'))
        self.topic = QTextEdit(self)
        self.topic.setGeometry(305, 30, 331, 51)
        self.topic.setPlaceholderText("Введите название")
        self.text = QTextEdit(self)
        self.text.setGeometry(45, 130, 871, 251)
        self.text.setPlaceholderText(
            "Вставьте текст. Слова должны состоять как минимум из 3 символов, предложения из 10")
        buttons_name = ['Слова', 'Предложения', 'Текст', 'Назад']
        buttons = []
        for i, name in enumerate(buttons_name):
            button = QPushButton(self)
            button.setGeometry(80 + i * 200, 410, 150, 40)
            button.setText(name)
            buttons.append(button)
        self.word_btn = buttons[0]
        self.sentences_btn = buttons[1]
        self.text_btn = buttons[2]
        self.close_btn = buttons[3]
        self.word_btn.clicked.connect(self.add_words)
        self.sentences_btn.clicked.connect(self.add_sentences)
        self.text_btn.clicked.connect(self.add_text)
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
        self.count_errors = 0
        self.count1_errors = 0
        self.dict_errors = []

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

        self.level_mode = QComboBox(self)
        self.level_mode.setGeometry(780, 220, 200, 60)
        self.level_mode.addItem("С ошибками")
        self.level_mode.addItem("Без ошибок")
        self.level_mode.addItem("Работа над ошибками")
        self.level_mode.activated[str].connect(self.block_change)
        
        self.sound_button = QPushButton(self)
        self.sound_button.setGeometry(780, 20, 35, 35)
        self.sound_button.clicked.connect(self.sound_on)
        self.sound_button.setIcon(QIcon("pictures/звук2.png"))
        self.sound_button.setStyleSheet('''QPushButton {
                                    background: white;
                                    border: 1px solid black;
                                    border-radius: 10px;
                                    border-width: 2px;
                                    font: bold 14px;
                              }''')

    def sound_off(self):
        self.sound_button.setIcon(QIcon("pictures/звук2.png"))
        self.sound_button.clicked.connect(self.sound_on)
        self.media_player.stop()

    def sound_on(self):
        self.media_player = QMediaPlayer()
        self.url = QUrl.fromLocalFile(QDir.toNativeSeparators("pictures/sound.mp3"))
        self.media_player.setMedia(QMediaContent(self.url))
        self.media_player.setVolume(50)
        self.media_player.play()
        self.sound_button.setIcon(QIcon("pictures/звук1.png"))
        self.sound_button.clicked.connect(self.sound_off)

    def block_change(self):
        if self.level_mode.currentText() == "Работа над ошибками":
            self.level_box.setDisabled(True)
        else:
            self.level_box.setDisabled(False)

    def set_stopwatch_interface(self):
        self.stopwatch = StopWatch()
        self.timer_label = QLabel(self)
        self.timer_label.setText('0:00.00')
        self.timer_label.setGeometry(330, 335, 75, 41)
        self.start = QPushButton(self)
        self.start.setGeometry(100, 320, 190, 71)
        self.start.setText("Старт")
        self.start.clicked.connect(self.start_session)
        self.start.clicked.connect(self.user_text_box.setFocus)
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
        self.CPM_value.setText("0 сим/мин")
        self.WPM = QLabel(self)
        self.WPM.setGeometry(750, 380, 150, 41)
        self.WPM.setText("WPM:")
        self.WPM_value = QLabel(self)
        self.WPM_value.setGeometry(890, 380, 90, 41)
        self.WPM_value.setText("0 слов/мин")

        self.errors = QLabel(self)
        self.errors.setGeometry(750, 420, 200, 41)
        self.errors.setText("Количество ошибок за сеанс:")
        self.errors_value = QLabel(self)
        self.errors_value.setGeometry(940, 420, 40, 41)
        self.errors_value.setText("0")

        self.errors1 = QLabel(self)
        self.errors1.setGeometry(750, 460, 150, 41)
        self.errors1.setText("Количество ошибок:")
        self.errors1_value = QLabel(self)
        self.errors1_value.setGeometry(890, 460, 90, 41)
        self.errors1_value.setText("0")


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
            if self.level_mode.currentText() == "Работа над ошибками":
                self.text_to_write.setText("")
                self.user_text_box.setText("")
                if len(self.dict_errors) == 0:
                    QMessageBox.information(self, "Ошибок нет", 'Выберите другой режим', QMessageBox.Ok)
                else:
                    self.text_to_write.setText(random.choice(sentences['ошибки']))
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
        save_results(str(datetime.datetime.now()).split(' ')[0],
                     self.stat.statistic['WPM'].value,
                     self.stat.statistic['CPM'].value,
                     int(self.errors_value.text()))
        if len(self.user_text_box.toPlainText()) != 0:
            self.user_text_box.clear()
        self.text_to_write.setText('')
        self.stat.nullify_result()
        self.stopwatch.do_finish()
        self.timer_label.setText('0:00.00')
        self.full_time_value.setText('0:00.00')
        self.full_stopwatch.do_finish()
        self.full_stopwatch.time = 0
        self.start.setText('Старт')
        self.WPM_value.setText("0 слов/мин")
        self.CPM_value.setText("0 сим/мин")
        self.errors_value.setText('0')
        self.count_errors = 0
        self.count1_errors = 0
        self.errors1_value.setText('0')

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
                if self.user_text_box.toPlainText() == self.text_to_write.toPlainText() \
                        and self.level_mode.currentText() == "С ошибками":
                    self.stat.statistic['WPM'].length += \
                        len(multiple_replace(self.user_text_box.toPlainText()).split(' '))
                    self.equal_strings()
                    self.count1_errors = 0
                if self.level_mode.currentText() == "Без ошибок":
                    self.stat.statistic['WPM'].length += \
                        len(multiple_replace(self.user_text_box.toPlainText()).split(' '))
                    self.equal_strings()
                    self.count1_errors = 0
                if self.level_mode.currentText() == "Работа над ошибками" \
                        and self.user_text_box.toPlainText() == self.text_to_write.toPlainText():
                    self.for_work_errors()
                    self.count1_errors = 0
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

    def for_work_errors(self):
        self.user_text_box.clear()
        self.stopwatch.do_finish()
        self.full_stopwatch.do_pause()
        self.symbols_state = []
        self.timer_label.setText('0:00.00')
        if self.text_to_write.toPlainText() in self.dict_errors:
            self.dict_errors.remove(self.text_to_write.toPlainText())
            sentences['ошибки'] = self.dict_errors
        if len(self.dict_errors) > 0:
            self.text_to_write.setText(random.choice(sentences['ошибки']))
        else:
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
        self.stat.process_data(self.full_time_value.text(), self.user_text_box.toPlainText())
        try:
            if self.symbols_state[-1][0] == "wrong":
                self.count_errors += 1
                self.count1_errors += 1
                if self.text_to_write.toPlainText() not in self.dict_errors:
                    if self.text_to_write.toPlainText().find(" ") != -1:
                        index = state_list[-1][1]
                        index1 = 0
                        index2 = 0
                        if self.text_to_write.toPlainText()[index] != ',' or ' ' or '-':
                            a = (self.text_to_write.toPlainText().replace(',', '')).replace('.', '')
                            for i in range(0, len(self.text_to_write.toPlainText())):
                                if a[index - i] == ' ':
                                    index1 = index - i
                                    break
                            for x in range(0, len(self.text_to_write.toPlainText())):
                                if a[index + x] == ' ':
                                    index2 = index + x
                                    break
                            if a[index1:index2].strip() not in self.dict_errors:
                                if index1 < 0:
                                    index1 = 0
                                self.dict_errors.append(a[index1:index2].strip())
                                self.dict_errors.remove("")
                    else:
                        self.dict_errors.append(self.text_to_write.toPlainText())
                dictionary.sentences["ошибки"] = list(set(self.dict_errors))
        except:
            IndexError

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
        self.CPM_value.setText(str(self.stat.statistic['CPM'].value) + ' сим/мин')
        self.WPM_value.setText(str(self.stat.statistic['WPM'].value) + ' слов/мин')
        self.errors_value.setText(str(self.count_errors))
        self.errors1_value.setText(str(self.count1_errors))

    @pyqtSlot()
    def set_color(self, state_list):
        """highlights valid and invalid characters"""
        cursor = self.text_to_write.textCursor()
        format = QTextCharFormat()
        if len(self.user_text_box.toPlainText()) <= len(self.text_to_write.toPlainText()):
            for char_text in range(len(state_list)):
                if state_list[char_text][0] == 'correct':
                    cursor.setPosition(state_list[char_text][1])
                    cursor.movePosition(cursor.Right, 1)
                    format.setBackground(QBrush(QColor('#a6f5c8')))
                    cursor.mergeCharFormat(format)
                elif state_list[char_text][0] == 'wrong':
                    cursor.setPosition(state_list[char_text][1])
                    cursor.movePosition(cursor.Right, 1)
                    format.setBackground(QBrush(QColor('#ff6e6e')))
                    cursor.mergeCharFormat(format)
            if len(state_list) <= len(self.symbols_state):
                for i in range(0, len(self.symbols_state)):
                    if i >= len(state_list):
                        cursor.setPosition(self.symbols_state[i][1])
                        cursor.movePosition(cursor.Right, 1)
                        format.setBackground(QBrush(QColor('#E6E6FA')))
                        cursor.mergeCharFormat(format)
            self.symbols_state = state_list
