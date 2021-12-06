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


class UsersStatistic:
    def __init__(self):
        self.data = take_results()
        self.wpm = []
        self.cpm = []
        self.errors = []
        self.stat = []
        self.x = []
        self.y = []
        self.y1 = []
        self.y2 = []

    def add_value(self):
        for i in range(len(self.data)):
            self.stat.append(self.data[i][0])
            self.wpm.append(self.data[i][1])
            self.cpm.append(self.data[i][2])
            self.errors.append(self.data[i][3])

    def get_figure(self):
        self.add_value()
        self.set_coordinates()
        figure = plt.figure(figsize=(17, 10))
        self.print_statistic("Wpm", 1, self.x, self.y)
        self.print_statistic("Cpm", 2, self.x, self.y1)
        self.print_statistic("Ошибки", 3, self.x, self.y2)
        figure.savefig("statistic.png")

    def set_coordinates(self):
        self.x = np.array(self.stat)
        self.y = np.array(self.wpm)
        self.y1 = np.array(self.cpm)
        self.y2 = np.array(self.errors)

    def print_statistic(self, title, plot, x, y):
        plt.subplot(2, 2, plot)
        plt.plot(x, y, '-', marker="o", c="g")
        plt.title(title)
        plt.grid()

