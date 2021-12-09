import unittest
import time
from modules import create_user_dict, load_dict
from modules.stopwatch import *
from modules.statistic import *
from data import *
import pytest


def test_stopwatch_sec_to_min():
    assert 1.0 == seconds_to_minutes('1:00.00')
    assert 1.9998333333333334 == seconds_to_minutes('01:59.99')
    assert 0.3333333333333333 == seconds_to_minutes('0:20.00')
    assert 0.004833333333333333 == seconds_to_minutes('0:00.29')


def test_stat():
    s = 'Самое замечательное число - 73. Вы скорее всего теряетесь в догадках почему.' \
        ' 73 — это 21-ое простое число. Его зеркальное отражение 37 является 12-ым, ' \
        'чье отражение 21 является результатом умножения, не упадите, 7 и 3. ' \
        'Ну, не обманул? Леонард: Убедил. Число 73 - Чак Норрис всем числам. Шелдон: ...' \
        'Чак Норрис нервно курит в сторонке.'
    stat = Statistic()
    stat.process_data('0:20.00', s)
    assert 159.0 == stat.statistic['WPM'].value
    stat.process_data('0:01.00', 'a')
    stat.process_data('0:02.00', 'b')
    stat.process_data('0:05.50', 'b')
    stat.process_data('0:07.81', 'b')
    stat.process_data('0:08.31', 'b')
    assert 43.0 == stat.statistic['CPM'].value


if __name__ == '__main__':
    unittest.main()
