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