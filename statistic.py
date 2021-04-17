from stopwatch import seconds_to_minutes


class Statistic:
    def __init__(self):
        self.statistic = {
            'WPM': WPM(),
            'claer_WPM': ClearWPM(),
            'CPM': CPM(),
            'clear_CPM': ClearCPM(),
            # 'KPM': KPM(),
            # 'clear_KPM': ClearKPM(),
        }

    def process_data(self, time, errors):
        for stat in self.statistic.values():
            stat.count_stat(time, errors)


class WPM:
    def __init__(self):
        self.value = 0

    def count_stat(self, time, errors):
        self.value += 0


class ClearWPM:
    def __init__(self):
        self.value = 0

    def count_stat(self, time, errors):
        pass


class CPM:
    def __init__(self):
        self.value = 0

    def count_stat(self, time, errors):
        self.value += (errors['errors_count'] + errors['count_symbols']) // seconds_to_minutes(time)


class ClearCPM:
    def __init__(self):
        self.value = 0

    def count_stat(self, time, errors):
        self.value += errors['count_symbols'] // seconds_to_minutes(time)


# class KPM:
#     def __init__(self):
#         self.value = 0
#
#     def count_stat(self, time, errors):
#         pass
#
#
# class ClearKPM:
#     def __init__(self):
#         self.value = 0
#
#     def count_stat(self, time, errors):
#         pass

