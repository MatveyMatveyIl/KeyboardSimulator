import unittest
import time
from modules import create_user_dict, dictionary
from modules.stopwatch import *
from modules.statistic import *
from data import *


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
                              'Ну, не обманул', 'Леонард: Убедил', 'Число 73 - Чак Норрис всем числам',
                              'Чак Норрис нервно курит в сторонке'],
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
        self.assertEqual(0.3333333333333333, seconds_to_minutes('0:20.00'), 10 ** -3)
        self.assertEqual(0.004833333333333333, seconds_to_minutes('0:00.29'))

    def test_stat(self):
        s = 'Самое замечательное число - 73. Вы скорее всего теряетесь в догадках почему.' \
            ' 73 — это 21-ое простое число. Его зеркальное отражение 37 является 12-ым, ' \
            'чье отражение 21 является результатом умножения, не упадите, 7 и 3. ' \
            'Ну, не обманул? Леонард: Убедил. Число 73 - Чак Норрис всем числам. Шелдон: ...' \
            'Чак Норрис нервно курит в сторонке.'
        self.stat = Statistic()
        self.stat.process_data('0:20.00', s)
        self.assertEqual(159.0, self.stat.statistic['WPM'].value)
        self.stat.process_data('0:01.00', 'a')
        self.stat.process_data('0:02.00', 'b')
        self.stat.process_data('0:05.50', 'b')
        self.stat.process_data('0:07.81', 'b')
        self.stat.process_data('0:08.31', 'b')
        self.assertEqual(43.0, self.stat.statistic['CPM'].value)

    def test_db(self):
        login_db()
        save_results('1.1.1', 1, 2, 3)
        self.assertEqual(('1.1.1', 1, 2, 3), *take_results())
        save_results('1.1.1', 5, 4, 3)
        save_results('1.1.1', 7, 7, 7)
        self.assertEqual(('1.1.1', 5, 5, 13), *take_results())
        save_results('1.1.2', 7, 7, 7)
        self.assertListEqual([('1.1.1', 5, 5, 13), ('1.1.2', 7, 7, 7)], take_results())
        #delete user.db


if __name__ == '__main__':
    unittest.main()
