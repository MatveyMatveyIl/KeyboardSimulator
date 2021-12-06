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
        self.x = np.array(self.stat)
        self.y = np.array(self.wpm)
        self.y1 = np.array(self.cpm)
        self.y2 = np.array(self.errors)

    def print_graph(self):
        for i in range(len(self.data)):
            self.stat.append(self.data[i][0])
            self.wpm.append(self.data[i][1])
            self.cpm.append(self.data[i][2])
            self.errors.append(self.data[i][3])

    def get_figure(self):
        plt.figure(figsize=(17, 7))
        figure = plt.get_current_fig_manager()
        figure.canvas.manager.set_window_title("Статистика")
        self.set_coordinates("Wpm", 1, self.x, self.y)
        self.set_coordinates("Cpm", 2, self.x, self.y1)
        self.set_coordinates("Ошибки", 3, self.x, self.y2)
        plt.show()

    @staticmethod
    def set_coordinates(title, plot, x, y):
        plt.subplot(2, 2, plot)
        plt.plot(x, y, '-', marker="o", c="g")
        plt.title(title)
        plt.grid()

# def print_graph_statistic(self):
#     date = []
#     wpm = []
#     cpm = []
#     errors = []
#     data = take_results()
#     for i in range(len(data)):
#         if len(data[i][0]) == 10:
#             date.append(data[i][0])
#             wpm.append(data[i][1])
#             cpm.append(data[i][2])
#             errors.append(data[i][3])
#     x = np.array(date)
#     y = np.array(wpm)
#     y1 = np.array(cpm)
#     y2 = np.array(errors)
#
#     plt.figure(figsize=(17, 7))
#     man = plt.get_current_fig_manager()
#     man.canvas.set_window_title("Статистика")
#     plt.subplot(221)
#     plt.plot(x, y, '-', marker="o", c="g")
#     plt.title("Wpm")
#     plt.grid()
#     plt.subplot(222)
#     plt.plot(x, y1, '-.', marker="o", c="b")
#     plt.title("Cpm")
#     plt.grid()
#     plt.subplot(223)
#     plt.plot(x, y2, '--', marker="o", c="r")
#     plt.title("Ошибки")
#     plt.grid()
#     plt.show()
#
#
# def print_graph_statistic1(self):
#     date1 = []
#     wpm1 = []
#     cpm1 = []
#     errors1 = []
#     data = take_results()
#     for i in range(len(data)):
#         if len(data[i][0]) != 10:
#             date1.append(((data[i][0]).split("."))[0])
#             wpm1.append(data[i][1])
#             cpm1.append(data[i][2])
#             errors1.append(data[i][3])
#     x1 = np.array(date1)
#     y11 = np.array(wpm1)
#     y111 = np.array(cpm1)
#     y21 = np.array(errors1)
#     plt.figure(figsize=(17, 7))
#     man = plt.get_current_fig_manager()
#     man.canvas.set_window_title("Статистика")
#     plt.subplot(221)
#     plt.plot(x1, y11, '-', marker="o", c="g")
#     plt.title("Wpm")
#     plt.grid()
#     plt.subplot(222)
#     plt.plot(x1, y111, '-.', marker="o", c="b")
#     plt.title("Cpm")
#     plt.grid()
#     plt.subplot(223)
#     plt.plot(x1, y21, '--', marker="o", c="r")
#     plt.title("Ошибки")
#     plt.grid()
#     plt.show()
