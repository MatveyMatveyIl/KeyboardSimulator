from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLineEdit, QLabel
import dictionary
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Keyboard simulator')
        self.setGeometry(500, 400, 600, 300)
        self.text_to_write = QLabel(self)
        self.level_text = iter(dictionary.sentences['easy'])
        self.text_to_write.setText(next(self.level_text))
        self.text_to_write.setGeometry(50, 100, 500, 40)
        self.textbox = QLineEdit(self)
        self.textbox.setGeometry(50, 200, 500, 40)
        self.textbox.returnPressed.connect(self.on_click)

    def on_click(self):
        if(self.textbox.text() == self.text_to_write.text()):
            print('OK!')
        else:
            print('Problem!')
        self.textbox.setText('')
        try:
            self.text_to_write.setText(next(self.level_text))
        except:
            StopIteration





app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())