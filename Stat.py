import matplotlib.pyplot as plt
import numpy as np
from data import take_results


class Stat:
    def __init__(self):
        super().__init__()
        # self.x = np.arange(-2*np.pi, 2*np.pi, 0.01)
        # self.y = np.sin(3*self.x)/self.x

    def showed(self):
        plt.grid(True)
        a = take_results()
        print(a)
        # plt.plot(self.x, self.y)
        # plt.show()

