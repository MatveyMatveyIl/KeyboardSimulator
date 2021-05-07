from modules.stopwatch import seconds_to_minutes
from modules.create_user_dict import multiple_replace


class Statistic:
    def __init__(self):
        self.statistic = {
            'WPM': WPM(),
            'CPM': CPM(),
        }

    def process_data(self, time, text):
        for stat in self.statistic.values():
            stat.count_stat(time, text)


class WPM:
    def __init__(self):
        self.value = 0
        self.length = 0
        self.time = 0
        self.count = 0

    def count_stat(self, time, text):
        multiple_replace(text)
        self.count = len(text.split(' ')) - 1
        self.time = seconds_to_minutes(time)
        if self.time != 0:
            self.value = (self.length + self.count) // self.time


class CPM:
    def __init__(self):
        self.value = 0
        self.length = 0
        self.time = 0

    def count_stat(self, time, text):
        self.length += 1
        self.time = seconds_to_minutes(time) if seconds_to_minutes(time) != 0 else 1
        self.value = self.length // self.time if self.length // self.time > 0 else 0
