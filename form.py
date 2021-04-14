import dictionary
import sys
import EXCEPTIONS
import form_style

try:
    from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
    from PyQt5.QtGui import QIcon
except Exception as e:
    print('PyQt5 not found: "{}".'.format(e))
    sys.exit(EXCEPTIONS.ERROR_QT_VERSION)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.level_text = iter(dictionary.sentences['easy'])
        self.set_user_interface()
        self._errors = []

    def set_user_interface(self):
        self.setWindowTitle('Keyboard simulator')
        self.setGeometry(500, 400, 600, 300)
        self.setWindowIcon(QIcon('pictures/programmIcon.png'))

        self.text_to_write = QLabel(self)
        self.text_to_write.setGeometry(50, 100, 500, 40)
        self.text_to_write.setText(next(self.level_text))

        self.user_text_box = QLineEdit(self)
        self.user_text_box.setGeometry(50, 200, 500, 40)
        self.user_text_box.returnPressed.connect(self.on_click_enter)
        self.user_text_box.textEdited.connect(self.check_errors)
        self.user_text_box.textEdited.connect(self.set_color)

    def on_click_enter(self):
        if self.user_text_box.text() == self.text_to_write.text():
            print('correct sentence:)')
            self.user_text_box.setText('')
            try:
                self.text_to_write.setText(next(self.level_text))
            except StopIteration:
                print('end of sentences')
        else:
            print('wrong sentence:(')

    def check_errors(self):
        self._errors = list(i for (i, (a, b)) in
                            enumerate(zip(self.text_to_write.text(),
                                          self.user_text_box.text()))
                            if a != b)

    def set_color(self):
        self.text_to_write.setStyleSheet('background-color: #a6f5c8')


app = QApplication(sys.argv)
#app.setStyleSheet(form_style.style)
window = Window()
window.show()
sys.exit(app.exec_())