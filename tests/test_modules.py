import unittest
import time
from modules import create_user_dict, dictionary
from modules.stopwatch import *
from PyQt5 import Qt


class TestModules(unittest.TestCase):
    def test_words(self):
        create_user_dict.create_words('aaaa, bv. cdd d: m, vamm? netA  chtoch-djdjd', 'words_new')
        self.assertListEqual(['aaaa', 'vamm', 'netA', 'chtoch', 'djdjd'], dictionary.sentences['words_new'])

    def test_sentences(self):
        s = 'Самое замечательное число - 73. Вы скорее всего теряетесь в догадках почему.' \
            ' 73 — это 21-ое простое число. Его зеркальное отражение 37 является 12-ым, ' \
            'чье отражение 21 является результатом умножения, не упадите, 7 и 3. ' \
            'Ну, не обманул? Леонард: Убедил. Число 73 - Чак Норрис всем числам. Шелдон: ...' \
            'Чак Норрис нервно курит в сторонке.'
        create_user_dict.create_sentences(s, 'sent')
        self.assertListEqual(['Самое замечательное число - 73',
                              'Вы скорее всего теряетесь в догадках почему',
                              '73 — это 21-ое простое число',
                              'Его зеркальное отражение 37 является 12-ым, чье отражение 21 является результатом умножения, не упадите, 7 и 3',
                              'Ну, не обманул', 'Леонард: Убедил', 'Число 73 - Чак Норрис всем числам', 'Чак Норрис нервно курит в сторонке'],
                             dictionary.sentences['sent'])

    def test_text(self):
        s = 'Самое замечательное число - 73. Вы скорее всего теряетесь в догадках почему.' \
            ' 73 — это 21-ое простое число. Его зеркальное отражение 37 является 12-ым, ' \
            'чье отражение 21 является результатом умножения, не упадите, 7 и 3. ' \
            'Ну, не обманул? Леонард: Убедил. Число 73 - Чак Норрис всем числам. Шелдон: ...' \
            'Чак Норрис нервно курит в сторонке.'
        create_user_dict.create_text(s, 'Text')
        self.assertListEqual([s], dictionary.sentences['Text'])

    def test_stopwatch_sec_to_min(self):
        self.assertEqual(1.0, seconds_to_minutes('1:00.00'))
        self.assertEqual(1.9998333333333334, seconds_to_minutes('01:59.99'))
        self.assertEqual(0.3333333333333333, seconds_to_minutes('0:20.00'), 10**-3)
        self.assertEqual(0.004833333333333333, seconds_to_minutes('0:00.29'))

    def test_stopwatch(self):
        # app = Qt.QCoreApplication([])
        # stopwatch = StopWatch()
        # stopwatch.do_start()
        # time.sleep(4)
        # print(stopwatch.time)
        #
        # from PyQt5.QtCore import QTimer
        # self.assertEqual(1, stopwatch.time)
        # app.exec_()
        pass


if __name__ == '__main__':
    unittest.main()
