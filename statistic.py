from stopwatch import seconds_to_minutes


class Statistic:
    def __init__(self):
        self.statistic = {
            'WPM': WPM(),
            'CPM': CPM(),
        }

    def process_data(self, time, errors, text):
        for stat in self.statistic.values():
            stat.count_stat(time, errors, text)


class WPM:
    def __init__(self):
        self.value = 0

    def count_stat(self, time, errors, text):
        self.value += len(text.split(' ')) // seconds_to_minutes(time)


class CPM:
    def __init__(self):
        self.value = 0

    def count_stat(self, time, errors, text):
        self.value += (errors['errors_count'] + errors['count_symbols']) // seconds_to_minutes(time)
