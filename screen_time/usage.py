#!/usr/bin/python3

import os
import datetime
import time

DIRECTORY = "/screen-time/"
WEEK_FILE = "week.txt"
LAST_WEEK_FILE = "last-week.txt"


class WeekUsage:

    def __init__(self):

        f = open(os.path.join(DIRECTORY, WEEK_FILE), "r")
        week_contents = f.read()
        f.close()

        f = open(os.path.join(DIRECTORY, LAST_WEEK_FILE), "r")
        last_week_contents = f.read()
        f.close()

        data_points = week_contents.split('\n')

        data = []

        for point in data_points:
            if point:
                try:
                    data.append(int(point))
                except ValueError:
                    pass

        data_points = last_week_contents.split('\n')

        for point in data_points:
            if point:
                try:
                    data.append(int(point))
                except ValueError:
                    pass

        days = [Usage(None, 0, 0) for i in range(7)]

        today = get_time()

        for i in range(7):
            i = 6 - i

            day = datetime.datetime.fromtimestamp(today) - datetime.timedelta(days=i)

            usage = get_sessions(data, day.timestamp())

            days[i].date = day.date()
            days[i].total_time = sum([d.get_length() for d in usage])
            days[i].unlocks = len(usage)

        self.days = list(reversed(days))


class Usage:

    def __init__(self, date, total_time, unlocks):
        self.total_time = total_time
        self.unlocks = unlocks
        self.date = date

    def __repr__(self):
        return format_time(self.total_time)


class TodayUsage:

    def __init__(self):

        f = open(os.path.join(DIRECTORY, WEEK_FILE), "r")
        contents = f.read()
        f.close()

        data_points = contents.split('\n')

        data = []

        for point in data_points:
            if point:
                try:
                    data.append(int(point))
                except ValueError:
                    pass

        today = get_time()

        self.sessions = get_sessions(data, today)

        self.unlocks = len(self.sessions)
        self.total_time = sum([d.get_length() for d in self.sessions])

    def get_total_time(self):
        return self.total_time

    def get_unlocks(self):
        return self.unlocks


class Duration:

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def get_length(self):
        return self.end_time - self.start_time

    def end(self):
        t = datetime.datetime.fromtimestamp(self.end_time)
        return t.hour * 60 + t.minute

    def start(self):
        t = datetime.datetime.fromtimestamp(self.start_time)
        return t.hour * 60 + t.minute

    def __repr__(self):
        return "{0} - {1}".format(readable_time_of_day(self.start_time), readable_time_of_day(self.end_time))


def format_time(total_time):
    hours = int(total_time / 3600)

    days = int(hours / 24)

    hours %= 24

    minutes = int((total_time % 3600) / 60)

    seconds = int(total_time % 60)

    output = ""

    if days:
        output += str(days) + "d "

    if hours:
        output += str(hours) + "h "

    if minutes:
        output += str(minutes) + "m "

    if not (minutes or hours):
        output += str(seconds) + "s"

    return output


def readable_time_of_day(time1):
    t1 = datetime.datetime.fromtimestamp(time1)
    return "{0}:{1:0>2}:{2:0>2}".format(t1.hour, t1.minute, t1.second)


def get_time():
    return int(time.time())


def on_same_date(time1, time2):
    t1 = datetime.datetime.fromtimestamp(time1)
    t2 = datetime.datetime.fromtimestamp(time2)

    return t1.date() == t2.date()


def condense_durations(times, difference):
    sessions = []
    times = sorted(times)
    if len(times) != 0:
        last_time = times[0]
        prev_time = times[0]

        for current_time in times:
            duration = Duration(prev_time, current_time)
            if duration.get_length() >= difference:
                # End session
                duration = Duration(last_time, prev_time)
                sessions.append(duration)
                last_time = current_time
            prev_time = current_time

        sessions.append(Duration(last_time, prev_time))
    return sessions


def get_sessions(data, day):
    data = list(filter(lambda p: on_same_date(day, p), data))

    return condense_durations(data, 4)
