from stopwatch import seconds_to_minutes
from create_user_dict import multiple_replace


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

    def count_stat(self, time, text):
        multiple_replace(text)
        self.value += len(text.split(' ')) // seconds_to_minutes(time)


class CPM:
    def __init__(self):
        self.value = 0

    def count_stat(self, time, text):
        self.value += len(text) // seconds_to_minutes(time)
