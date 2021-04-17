from PyQt5 import Qt
import pyqtgraph as pg
import numpy as np


class Window(Qt.QWidget):

    def __init__(self):
        super().__init__()

        layout = Qt.QVBoxLayout(self)

        self.view = view = pg.PlotWidget()
        self.curve = view.plot(name="Line")

        self.btn = Qt.QPushButton("Random plot")
        self.btn.clicked.connect(self.random_plot)

        layout.addWidget(Qt.QLabel("Some text"))
        layout.addWidget(self.view)
        layout.addWidget(self.btn)

    def random_plot(self):
        random_array = np.random.random_sample(20)
        self.curve.setData(random_array)


if __name__ == "__main__":
    app = Qt.QApplication([])
    w = Window()
    w.show()
    app.exec()
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPlainTextEdit, QVBoxLayout
# from PyQt5.QtCore import QRegExp
# from PyQt5.QtGui import QColor, QRegExpValidator, QSyntaxHighlighter, QTextCharFormat
#
# class SyntaxHighlighter(QSyntaxHighlighter):
#     def __init__(self, parnet):
#         super().__init__(parnet)
#         self.errors = {}
#
#     def highlight_line(self, line_num, fmt):
#         if isinstance(line_num, int) and line_num >= 0 and isinstance(fmt, QTextCharFormat):
#             self.errors[line_num] = fmt
#             block = self.document().findBlockByNumber(line_num)
#             self.rehighlightBlock(block)
#
#     def clear_highlight(self):
#         self.errors = {}
#         self.rehighlight()
#
#     def highlightBlock(self, text):
#         blockNumber = self.currentBlock().blockNumber()
#         fmt = self.errors.get(blockNumber)
#         if fmt is not None:
#             self.setFormat(0, 1, fmt)
#
# class AppDemo(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.resize(1200, 800)
#
#         mainLayout = QVBoxLayout()
#
#         validator = QRegExpValidator(QRegExp(r'[0-9]+'))
#
#         self.lineEdit = QLineEdit()
#         self.lineEdit.setStyleSheet('font-size: 30px; height: 50px;')
#         self.lineEdit.setValidator(validator)
#         self.lineEdit.textChanged.connect(self.onTextChanged)
#         mainLayout.addWidget(self.lineEdit)
#
#         self.textEditor = QPlainTextEdit()
#         self.textEditor.setStyleSheet('font-size: 30px; color: green')
#         mainLayout.addWidget(self.textEditor)
#
#         # for i in range(1, 21):
#         #     self.textEditor.appendPlainText('Line {0}'.format(i))
#
#         self.highlighter = SyntaxHighlighter(self.textEditor.document())
#         self.setLayout(mainLayout)
#
#     def onTextChanged(self, text):
#         fmt = QTextCharFormat()
#         fmt.setBackground(QColor('yellow'))
#
#         self.highlighter.clear_highlight()
#
#         try:
#             lineNumber = int(text) - 1
#             self.highlighter.highlight_line(lineNumber, fmt)
#         except ValueError:
#             pass
#
# app = QApplication(sys.argv)
# demo = AppDemo()
# demo.show()
# sys.exit(app.exec_())


# self._errors = list(i for (i, (a, b)) in
        #                     enumerate(zip(self.text_to_write.toPlainText(),
        #                                   self.user_text_box.text()))
        #                     if a != b)


# @pyqtSlot()
    # def on_click_enter(self):
    #     #if self.user_text_box.toPlainText() == self.text_to_write.toPlainText():
    #     if self.user_text_box.text() == self.text_to_write.toPlainText():
    #         self.user_text_box.clear()
    #         self.stopwatch.do_pause()
    #         self.timer_label.setText('0:00.00')
    #         try:
    #             self.text_to_write.setText(next(self.level_text))
    #             print('correct')
    #         except StopIteration:
    #             print('wrong')
    #             pass #message


# def set_user_text_box_interface(self):
#     self.user_text_box = QLineEdit(self)
#     self.user_text_box.setGeometry(50, 360, 701, 291)
#     self.user_text_box.returnPressed.connect(self.on_click_enter)
#     self.user_text_box.textChanged.connect(self.check_errors)
#     self.user_text_box.textChanged.connect(self.update_time)

# self.count_wrong_words = list(i for (i, (a, b)) in
#                                               enumerate(zip(self.user_text_box.toPlainText().split(' '),
#                                                             self.text_to_write.toPlainText().split(' ')))
#                                               if a != b)