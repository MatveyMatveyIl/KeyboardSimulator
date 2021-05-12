from modules.stopwatch import seconds_to_minutes
from modules.create_user_dict import multiple_replace
import matplotlib.pyplot as plt
import numpy as np
from data import take_results


class Statistic:
    def __init__(self):
        self.statistic = {
            'WPM': WPM(),
            'CPM': CPM(),
        }

    def process_data(self, time, text):
        for stat in self.statistic.values():
            stat.count_stat(time, text)

    def nullify_result(self):
        for stat in self.statistic.values():
            stat.length = 0
            stat.value = 0
            stat.time = 0
        self.statistic['WPM'].count = 0


class WPM:
    def __init__(self):
        self.value = 0
        self.length = 0
        self.time = 0
        self.count = 0

    def count_stat(self, time, text):
        multiple_replace(text)
        self.count = len(text.split(' ')) - 1
        self.time = seconds_to_minutes(time) if seconds_to_minutes(time) != 0 else 1
        self.value = (self.length + self.count) // self.time


class CPM:
    def __init__(self):
        self.value = 0
        self.length = 0
        self.time = 0

    def count_stat(self, time, text):
        self.length += 1
        self.time = seconds_to_minutes(time) if seconds_to_minutes(time) != 0 else 1
        self.value = self.length // self.time


def print_graph_statistic(self):
    date = []
    wpm = []
    cpm = []
    errors = []
    data = take_results()
    for i in range(len(data)):
        date.append(data[i][0])
        wpm.append(data[i][1])
        cpm.append(data[i][2])
        errors.append(data[i][3])
    x = np.array(date)
    y = np.array(wpm)
    y1 = np.array(cpm)
    y2 = np.array(errors)
    plt.figure(figsize=(17, 7))
    man = plt.get_current_fig_manager()
    man.canvas.set_window_title("Статистика")
    plt.subplot(221)
    plt.plot(x, y, '-', marker="o", c="g")
    plt.title("Wpm")
    plt.grid()
    plt.subplot(222)
    plt.plot(x, y1, '-.', marker="o", c="b")
    plt.title("Cpm")
    plt.grid()
    plt.subplot(223)
    plt.plot(x, y2, '--', marker="o", c="r")
    plt.title("Ошибки")
    plt.grid()
    plt.show()