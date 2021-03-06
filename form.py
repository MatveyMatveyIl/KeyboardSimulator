import sys
from modules.load_dict import load_dict, update_dict
import random
from modules import statistic
from modules import form_style
from modules.stopwatch import *
from modules.create_user_dict import *
import datetime
from data import *
import matplotlib.pyplot as plt
import numpy as np

from PyQt5.QtWidgets import QApplication, QMainWindow, \
    QLineEdit, QLabel, QComboBox, QMenuBar, QMenu, QAction, QTextEdit, QPlainTextEdit, QWidget, QPushButton, \
    QMessageBox, QInputDialog
from PyQt5.QtGui import QIcon, QTextCharFormat, QFont, QSyntaxHighlighter, QColor, QBrush, QRegion, QPixmap
from PyQt5.QtCore import QTimer, pyqtSlot, QEvent, QRegularExpression, Qt, QRegExp, QUrl, QDir
from PyQt5.QtMultimedia import QMultimedia, QMediaPlayer, QMediaContent, QSound


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Keyboard simulator')
        self.setFixedSize(380, 350)
        self.setWindowIcon(QIcon('pictures_and_music/programmIcon.png'))
        buttons_name = ['Помощь', 'Статистика', 'Словари', 'Старт']
        buttons = []
        for i, name in enumerate(buttons_name):
            button = QPushButton(self)
            button.setGeometry(50, 30 + 80 * i, 260, 50)
            button.setText(name)
            buttons.append(button)
        self.helper = buttons[0]
        self.stat = buttons[1]
        self.add_text = buttons[2]
        self.button_start = buttons[3]

    def show_main_window(self):
        windows = {'keyboard': WindowKeyboardTrainer(), 'add_text': AddTextWindow(), 'helper': AddHelperWindow(),
                   'stat': CheckStat()}
        self.main_window = MainWindow()
        self.main_window.button_start.clicked.connect(lambda: self.show_window(windows['keyboard']))
        self.main_window.button_start.clicked.connect(self.main_window.close)
        self.main_window.add_text.clicked.connect(lambda: self.show_window(windows['add_text']))
        self.main_window.add_text.clicked.connect(self.main_window.close)
        self.main_window.stat.clicked.connect(lambda: self.show_window(windows['stat']))
        self.main_window.helper.clicked.connect(lambda: self.show_window(windows['helper']))
        self.main_window.show()

    def show_window(self, name):
        self.window = name
        self.window.show()


class CheckStat(QWidget):
    def __init__(self):
        super(CheckStat, self).__init__()
        self.user_stat = statistic.UsersStatistic()
        self.setWindowTitle('Keyboard simulator')
        self.setFixedSize(190, 170)
        self.setWindowIcon(QIcon('pictures_and_music/programmIcon.png'))
        self.stat_of_days = QPushButton(self)
        self.stat_of_days.setGeometry(10, 50, 170, 50)
        self.stat_of_days.setText("По дням")
        self.stat_of_days.clicked.connect(self.show_window)
        self.stat_of_days.clicked.connect(self.close)

    def show_window(self):
        self.window = StatisticGraph()
        self.window.show()


class StatisticGraph(QWidget):
    def __init__(self):
        super(StatisticGraph, self).__init__()
        statistic.UsersStatistic().get_figure()
        image_label = QLabel(self)
        pixmap = QPixmap("statistic.png")
        image_label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())
        self.setWindowTitle('Статистика')

class AddHelperWindow(QWidget):
    def __init__(self):
        super(AddHelperWindow, self).__init__()
        self.setWindowTitle('Keyboard simulator')
        self.setFixedSize(970, 465)
        self.setWindowIcon(QIcon('pictures_and_music/programmIcon.png'))
        self.help = QLabel(self)
        self.help.setGeometry(10, 10, 950, 440)
        self.help.setText("\n 1.Чтобы начать тренировку нажмите кнопку 'Старт' в меню \n \n"
                          " 2.Выберите один из режимов тренировки:"
                          "\n \n    - С ошибками (Вы можете не исправлять свои ошибки)"
                          "\n    - Без ошибок (Вы не продвинетесь с места, пока не исправите ошибки в тексте)"
                          "\n    - Работа над ошибками (Вы можете посмотреть в каих словах была допущена ошибка и "
                          "исправить их) \n "
                          "\n 3.Выберите словарь: слова, предложение или текст, также вы можете добавить свой "
                          "словарь.\n "
                          " Для этого в меню нажмите 'Добавить текст', введите название словаря и сам текст \n"
                          "\n 4.При желании вы можете выбрать музыку, которая будет сопровождать тренировку\n"
                          "\n 5.Нажмите 'Старт'\n"
                          "\n 6.Вы можете нажать 'Пауза', чтобы приостановить тренировку, затем 'Продолжить' \n"
                          "\nПо каждой сессии выводится статистика, вы можете ее увидеть справа в окне тренировки \n"
                          "\nГрафик статистки вы можете посмотреть, нажав 'Статистика' в меню \n"
                          "\nПри завершении тренировки не забудьте нажать 'Завершить и сохранить'")
        self.help.setWordWrap(True)
        self.help.setStyleSheet('''QLabel {
                                                font: Arial;
                                                font: 16px;
                                                qproperty-alignment: AlignLeft;
                                          }''')


class AddTextWindow(QWidget):
    def __init__(self):
        self.sentences = load_dict()
        super(AddTextWindow, self).__init__()
        self.setWindowTitle('Keyboard simulator')
        self.setFixedSize(970, 465)
        self.setWindowIcon(QIcon('pictures_and_music/programmIcon.png'))
        self.topic = QTextEdit(self)
        self.topic.setGeometry(45, 30, 330, 50)
        self.topic.setPlaceholderText("Введите название")
        self.text = QTextEdit(self)
        self.text.setGeometry(45, 130, 870, 250)
        self.text.setPlaceholderText(
            "Вставьте текст. Слова должны состоять как минимум из 3 символов, предложения из 10")
        self.dicts = QComboBox(self)
        self.dicts.setGeometry(400, 30, 330, 50)
        for name in self.sentences.keys():
            self.dicts.addItem(name)
        self.delete_btn = QPushButton(self)
        self.delete_btn.setGeometry(750, 30, 100, 50)
        self.delete_btn.setText('Удалить')
        self.delete_btn.clicked.connect(self.delete_dict)
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
        if self.critical_text():
            create_words(self.text.toPlainText(), self.topic.toPlainText(), self.sentences)
            update_dict(self.sentences)
            self.update_names_dict()

    def add_sentences(self):
        if self.critical_text():
            create_sentences(self.text.toPlainText(), self.topic.toPlainText(), self.sentences)
            update_dict(self.sentences)
            self.update_names_dict()

    def add_text(self):
        if self.critical_text():
            create_text(self.text.toPlainText(), self.topic.toPlainText(), self.sentences)
            update_dict(self.sentences)
            self.update_names_dict()

    def delete_dict(self):
        delete_key(self.dicts.currentText(), self.sentences)
        update_dict(self.sentences)
        self.update_names_dict()
        QMessageBox.information(self, "Успешно", "Словарь удален", QMessageBox.Ok)

    def update_names_dict(self):
        self.dicts.clear()
        for name in self.sentences.keys():
            self.dicts.addItem(name)

    def critical_text(self):
        if len(self.text.toPlainText()) == 0:
            QMessageBox.critical(self, "Ошибка", "Вы не ввели текст", QMessageBox.Ok)
            return False
        elif len(self.topic.toPlainText()) == 0:
            QMessageBox.critical(self, "Ошибка", "Введите название", QMessageBox.Ok)
            return False
        else:
            QMessageBox.information(self, "Успешно", "Словарь создан", QMessageBox.Ok)
            return True


class WindowKeyboardTrainer(QMainWindow):
    def __init__(self):
        super(WindowKeyboardTrainer, self).__init__()
        self.dictionaries = load_dict()
        self.set_user_interface()
        self.stat = statistic.Statistic()
        self.full_stopwatch = StopWatch()
        self.symbols_state = []
        self.count_all_errors = set()
        self.count_all_errors_value = 0
        self.count_errors = set()
        self.errors_session = []
        self.text_to_write_value = ''
        self.current_level_box = ''

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
        self.setWindowIcon(QIcon('pictures_and_music/programmIcon.png'))

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
        for topic in self.dictionaries.keys():
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
        self.sound_button.setIcon(QIcon("pictures_and_music/звук2.png"))
        self.sound_button.setStyleSheet('''QPushButton {
                                    background: white;
                                    border: 1px solid black;
                                    border-radius: 10px;
                                    border-width: 2px;
                                    font: bold 14px;
                              }''')
        self.level_sound = QComboBox(self)
        self.level_sound.setStyleSheet('''QComboBox {
                                         font: Arial;
                                         font:12px;
                                   }''')
        self.level_sound.setGeometry(830, 20, 150, 50)
        self.level_sound.addItem("Выберите музыку")
        self.level_sound.addItem("AC/DC")
        self.level_sound.addItem("Antonio Vivaldi")
        self.level_sound.addItem("Gorillaz")
        self.level_sound.activated[str].connect(self.check_level_sound)

    def check_level_sound(self):
        if self.level_sound.currentText() == "AC/DC":
            self.sound_play("pictures_and_music/sound3.wav")
        if self.level_sound.currentText() == "Antonio Vivaldi":
            self.sound_play("pictures_and_music/sound4.wav")
        if self.level_sound.currentText() == "Gorillaz":
            self.sound_play("pictures_and_music/sound5.wav")
        if self.level_sound.currentText() == "Выберите музыку":
            self.sound_off()
        self.sound_button.setIcon(QIcon("pictures_and_music/звук1.png"))
        self.sound_button.clicked.connect(self.sound_off)

    def sound_play(self, sound):
        self.media_player = QSound(sound)
        self.media_player.play()

    def sound_off(self):
        if self.level_sound.currentText() != "Выберите музыку":
            self.sound_button.setIcon(QIcon("pictures_and_music/звук2.png"))
            self.sound_button.clicked.connect(self.sound_on)
            self.media_player.stop()

    def sound_on(self):
        if self.level_sound.currentText() != "Выберите музыку":
            self.media_player.play()
        self.sound_button.setIcon(QIcon("pictures_and_music/звук1.png"))
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
        buttons_name = ['Старт', 'Завершить и сохранить']
        buttons = []
        for i, name in enumerate(buttons_name):
            button = QPushButton(self)
            button.setGeometry(100 + i * 320, 320, 190, 70)
            button.setText(name)
            buttons.append(button)
        self.start = buttons[0]
        self.finish = buttons[1]
        self.start.clicked.connect(self.start_session)
        self.start.clicked.connect(self.user_text_box.setFocus)
        self.finish.clicked.connect(self.end_session)
        label_names = [('Время сеанса:', '00:00:00'), ('CPM:', '0 сим/мин'),
                       ('WPM:', '0 слов/мин'), ('Ошибок за сеанс:', '0'), ('Количество ошибок:', '0')]
        labels = []
        for i, name in enumerate(label_names):
            label = QLabel(self)
            label_value = QLabel(self)
            if name == 'Количество ошибок за сеанс:':
                label.setGeometry(750, 300 + 40 * i, 200, 40)
                label_value.setGeometry(940, 300 + 40 * i, 40, 40)
            else:
                label.setGeometry(750, 300 + 40 * i, 150, 40)
                label_value.setGeometry(890, 300 + 40 * i, 90, 40)
            label.setText(name[0])
            label_value.setText(name[1])
            labels.append((label, label_value))
        self.full_time_label, self.full_time_value = labels[0][0], labels[0][1]
        self.CPM, self.CPM_value = labels[1][0], labels[1][1]
        self.WPM, self.WPM_value = labels[2][0], labels[2][1]
        self.all_errors, self.all_errors_value = labels[3][0], labels[3][1]
        self.errors, self.errors_value = labels[4][0], labels[4][1]

    def start_session(self):
        """Session start/pause handling"""
        if self.start.text() in {'Старт', 'Продолжить'}:
            self.user_text_box.setReadOnly(False)
            self.level_box.setDisabled(True)
            if self.full_time_value != '0:00.00' and len(self.user_text_box.toPlainText()) != 0:
                self.stopwatch.do_start()
                self.full_stopwatch.do_start()
            if len(self.text_to_write.toPlainText()) == 0:
                self.current_level_box = self.level_box.currentText()
                self.text_to_write.setText(random.choice(self.dictionaries[self.current_level_box]))
                self.text_to_write_value = self.text_to_write.toPlainText()
            if self.level_mode.currentText() == "Работа над ошибками":
                self.text_to_write.clear()
                self.user_text_box.clear()
                if len(self.errors_session) == 0:
                    QMessageBox.information(self, "Ошибок нет", 'Выберите другой режим', QMessageBox.Ok)
                else:
                    self.text_to_write.setText(random.choice(self.dictionaries['ошибки']))
            if self.current_level_box != self.level_box.currentText():
                self.user_text_box.clear()
                self.current_level_box = self.level_box.currentText()
                self.text_to_write.setText(random.choice(self.dictionaries[self.current_level_box]))
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
        save_results(datetime.datetime.now().date(),
                     self.stat.statistic['WPM'].value,
                     self.stat.statistic['CPM'].value,
                     int(self.all_errors_value.text()))
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
        self.all_errors_value.setText('0')
        self.count_all_errors.clear()
        self.count_errors.clear()
        self.errors_value.setText('0')

    def set_menubar_interface(self):
        self.menu = QPushButton(self)
        self.menu.setGeometry(760, 610, 221, 41)
        self.menu.setText("Выход в меню")
        self.menu.clicked.connect(self.save_before_exit)
        self.menu.clicked.connect(self.sound_off)

    def save_before_exit(self):
        if self.stat.statistic['WPM'] != 0 or self.stat.statistic['CPM'] != 0:
            save_results(datetime.datetime.now().date(),
                         self.stat.statistic['WPM'].value,
                         self.stat.statistic['CPM'].value,
                         int(self.all_errors_value.text()))
            self.stat.nullify_result()
        self.main_window = MainWindow()
        self.main_window.show_main_window()
        self.close()

    def eventFilter(self, obj, event):
        """Check input if pressed key is Enter"""
        if event.type() == QEvent.KeyPress and obj is self.user_text_box:
            if event.key() == Qt.Key_Return and self.user_text_box.hasFocus():
                if self.user_text_box.toPlainText() == self.text_to_write_value \
                        and self.level_mode.currentText() == "С ошибками":
                    self.equal_strings()
                if self.level_mode.currentText() == "Без ошибок":
                    self.equal_strings()
                if self.level_mode.currentText() == "Работа над ошибками" \
                        and self.user_text_box.toPlainText() == self.text_to_write.toPlainText():
                    self.for_work_errors()
                    self.count_errors.clear()
                return True
        return False

    def equal_strings(self):
        self.user_text_box.clear()
        self.stopwatch.do_finish()
        self.full_stopwatch.do_pause()
        self.symbols_state = []
        self.timer_label.setText('0:00.00')
        self.stat.statistic['WPM'].length += \
            len(multiple_replace(self.user_text_box.toPlainText()).split(' '))
        self.count_all_errors_value += len(self.count_all_errors)
        self.count_errors.clear()
        self.count_all_errors.clear()
        self.text_to_write.setText(random.choice(self.dictionaries[self.current_level_box]))
        self.text_to_write_value = self.text_to_write.toPlainText()

    def for_work_errors(self):
        self.user_text_box.clear()
        self.stopwatch.do_finish()
        self.full_stopwatch.do_pause()
        self.symbols_state = []
        self.timer_label.setText('0:00.00')
        if self.text_to_write.toPlainText() in self.errors_session:
            self.errors_session.remove(self.text_to_write.toPlainText())
            self.dictionaries['ошибки'] = self.errors_session
        if len(self.errors_session) > 0:
            self.text_to_write.setText(random.choice(self.dictionaries['ошибки']))
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
        self.add_errors(state_list)

    def add_errors(self, state_list):
        try:
            if self.symbols_state[-1][0] == "wrong":
                self.count_all_errors.add(self.symbols_state[-1][1])
                self.count_errors.add(self.symbols_state[-1][1])
                if self.text_to_write_value not in self.errors_session:
                    if self.text_to_write_value.find(" ") != -1:
                        index = state_list[-1][1]
                        if self.text_to_write_value[index] != ',' or ' ' or '-':
                            index1 = self.text_to_write_value.find(' ', index)
                            index1 = len(self.text_to_write_value) if index1 == -1 else index1
                            index2 = self.text_to_write_value[::-1].find(' ',
                                                                         len(self.text_to_write_value) - index)
                            index2 = 0 if index2 == - 1 else len(self.text_to_write_value) - index2
                            if self.text_to_write_value[index2:index1].strip() not in self.errors_session:
                                self.errors_session.append(
                                    self.text_to_write_value[index2:index1].strip())
                                print(self.errors_session)
                    else:
                        self.errors_session.append(self.text_to_write_value)
                self.dictionaries["ошибки"] = list(set(self.errors_session))
        except Exception as e:
            pass

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
        self.all_errors_value.setText(str(len(self.count_all_errors) + self.count_all_errors_value))
        self.errors_value.setText(str(len(self.count_errors)))

    @pyqtSlot()
    def set_color(self, state_list):
        """highlights valid and invalid characters"""
        cursor = self.text_to_write.textCursor()
        format = QTextCharFormat()
        if len(self.user_text_box.toPlainText()) <= len(self.text_to_write.toPlainText()):
            for char_text in range(len(state_list)):
                if state_list[char_text][0] == 'correct':
                    if char_text < len(self.symbols_state):
                        if state_list[char_text] == self.symbols_state[char_text]:
                            continue
                    cursor.setPosition(state_list[char_text][1])
                    cursor.movePosition(cursor.Right, 1)
                    format.setBackground(QBrush(QColor('#a6f5c8')))
                    cursor.mergeCharFormat(format)
                elif state_list[char_text][0] == 'wrong':
                    if char_text < len(self.symbols_state):
                        if state_list[char_text] == self.symbols_state[char_text]:
                            continue
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
