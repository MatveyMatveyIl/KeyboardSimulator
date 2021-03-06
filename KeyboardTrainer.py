from form import *
from data import Session


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(form_style.style)
    window = MainWindow()
    window.show()
    window.close()
    window.show_main_window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()