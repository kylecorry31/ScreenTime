#!/usr/bin/env python

import argparse
import os
import time
import datetime

FOLDER = "/screen-time/"
THIS_WEEK_FILENAME = "week.txt"
LAST_WEEK_FILENAME = "last-week.txt"


def daemon(folder, delay):
    print "Logging screen time in the background."
    create_directory(folder)

    this_week_path = os.path.join(folder, THIS_WEEK_FILENAME)
    last_week_path = os.path.join(folder, LAST_WEEK_FILENAME)

    create_file(this_week_path)
    create_file(last_week_path)

    week_file = open(this_week_path, "r")

    time.sleep(delay)

    last_updated = get_time()

    if week_file:
        # Read the first line of the week file
        file_time = week_file.readline()
        week_file.close()

        if file_time:
            file_time = int(file_time)

            if not on_same_week(file_time, last_updated):
                # Save week file to archive
                copy_file(this_week_path, last_week_path)

                # Erase week file contents
                erase_file_contents(this_week_path)

    while True:
        # In case it gets deleted
        create_directory(folder)
        create_file(this_week_path)
        create_file(last_week_path)

        current_time = get_time()
        append_file(this_week_path, str(current_time) + "\n")

        if not on_same_week(current_time, last_updated):
            # Save week file to archive
            copy_file(this_week_path, last_week_path)

            # Erase week file contents
            erase_file_contents(this_week_path)

        time.sleep(delay)


# Date-Time Utils
def get_time():
    return int(time.time())


def on_same_date(time1, time2):
    t1 = datetime.datetime.fromtimestamp(time1)
    t2 = datetime.datetime.fromtimestamp(time2)

    return t1.date() == t2.date()


def get_year(m_time):
    return datetime.datetime.fromtimestamp(m_time).year


def get_week_number(m_time):
    return datetime.datetime.fromtimestamp(m_time).isocalendar()[1]


def on_same_week(time1, time2):
    if on_same_date(time1, time2):
        return True

    return get_year(time1) == get_year(time2) and get_week_number(time1) == get_week_number(time2)


# FILE UTILS
def create_file(file_path):
    try:
        f = open(file_path, "a+")
        f.close()
    except Exception:
        pass


def create_directory(path):
    try:
        os.makedirs(path)
    except OSError:
        pass


def copy_file(src_path, dest_path):
    try:
        src_file = open(src_path, "r")
        dest_file = open(dest_path, "w+")

        dest_file.write(src_file.read())

        dest_file.close()
        src_file.close()
    except Exception:
        pass


def erase_file_contents(path):
    try:
        f = open(path, "w+")
        f.close()
    except Exception:
        pass


def append_file(path, text):
    try:
        f = open(path, "a+")
        f.write(text)
        f.close()
    except Exception:
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", "-d",
                        help="The directory to write files to.", type=str, default=FOLDER)
    parser.add_argument("--interval", "-i",
                        help="The recording interval time in seconds. Defaults to 1 second.", type=float, default=1)
    args = parser.parse_args()
    daemon(args.directory, args.interval)
