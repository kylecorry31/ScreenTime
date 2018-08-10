#!/usr/bin/env python

import argparse
import os
import time
import datetime

FOLDER = "/screen-time/"
THIS_WEEK_FILENAME = "week.txt"
LAST_WEEK_FILENAME = "last-week.txt"


def daemon(folder):
    try:
        os.makedirs(folder)
    except OSError:
        pass

    create_file(os.path.join(folder, THIS_WEEK_FILENAME))
    create_file(os.path.join(folder, LAST_WEEK_FILENAME))

    week_file = open(os.path.join(folder, THIS_WEEK_FILENAME), "a+")

    delay = 1

    time.sleep(delay)

    last_updated = get_time()

    if week_file:
        # Read the first line of the week file and then reset
        file_time = week_file.readline()
        week_file.seek(0)

        if file_time:
            file_time = int(file_time)

            if not on_same_week(file_time, last_updated):
                # Save week file to archive
                archive_file = open(os.path.join(folder, LAST_WEEK_FILENAME), "w")
                archive_file.write(week_file.read())
                archive_file.close()

                # Erase week file contents
                week_file.close()
                week_file = open(os.path.join(folder, THIS_WEEK_FILENAME), "w")
                week_file.close()

        week_file.close()

    while True:

        week_file = open(os.path.join(folder, THIS_WEEK_FILENAME), "a")
        current_time = get_time()
        week_file.write(str(current_time) + "\n")
        week_file.close()

        if not on_same_week(current_time, last_updated):
            week_file = open(os.path.join(folder, THIS_WEEK_FILENAME), "r")
            # Save week file to archive
            archive_file = open(os.path.join(folder, LAST_WEEK_FILENAME), "w")
            archive_file.write(week_file.read())
            archive_file.close()

            # Erase week file contents
            week_file = open(os.path.join(folder, THIS_WEEK_FILENAME), "w")
            week_file.close()

        time.sleep(delay)


def create_file(file_path):
    f = open(file_path, "a+")
    f.close()


def get_time():
    return int(time.time())


def on_same_date(time1, time2):
    t1 = datetime.datetime.fromtimestamp(time1)
    t2 = datetime.datetime.fromtimestamp(time2)

    return t1.date() == t2.date()


def on_same_week(time1, time2):
    if on_same_date(time1, time2):
        return True

    t1 = datetime.datetime.fromtimestamp(time1)
    t2 = datetime.datetime.fromtimestamp(time2)

    return t1.date().isocalendar()[1] == t2.date().isocalendar()[1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", "-d",
                        help="The directory to write files to.", type=str, default=FOLDER)
    args = parser.parse_args()
    daemon(args.directory)
