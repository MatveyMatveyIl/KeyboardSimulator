import matplotlib.pyplot as plt
import numpy as np
from data import take_results


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

