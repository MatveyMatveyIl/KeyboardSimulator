from form import *


app = QApplication(sys.argv)
app.setStyleSheet(form_style.style)
window = MainWindow()
window.show()
window.close()
window.show_main_window()
sys.exit(app.exec_())