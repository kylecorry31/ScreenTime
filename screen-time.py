#!/usr/bin/env python2

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

    time.sleep(delay)

    last_updated = get_time()

    week_file = open(this_week_path, "r")

    if week_file:
        # Read the first line of the week file
        file_time = week_file.readline()
        week_file.close()

        if file_time:
            file_time = int(file_time)

            if should_archive(last_updated, file_time):
                archive(this_week_path, last_week_path)
                print "Archiving week file."

    while True:
        # In case it gets deleted
        create_directory(folder)
        create_file(this_week_path)
        create_file(last_week_path)

        current_time = get_time()
        append_file(this_week_path, str(current_time) + "\n")

        if should_archive(current_time, last_updated):
            archive(this_week_path, last_week_path)
            print "Archiving week file."

        last_updated = current_time
        time.sleep(delay)


# Helpers
def archive(this_week_path, last_week_path):
    copy_file(this_week_path, last_week_path)
    erase_file_contents(this_week_path)
    

def should_archive(current_time, last_updated):
    return not on_same_week(current_time, last_updated)


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


# File Utils
def create_file(file_path):
    try:
        f = open(file_path, "a+")
        f.close()
    except Exception:
        print "Could not create file:", file_path


def create_directory(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError:
        print "Could not create directory:", path


def copy_file(src_path, dest_path):
    try:
        src_file = open(src_path, "r")
        dest_file = open(dest_path, "w+")

        dest_file.write(src_file.read())

        dest_file.close()
        src_file.close()
    except Exception:
        print "Could not copy", src_path, "to", dest_path


def erase_file_contents(path):
    try:
        f = open(path, "w+")
        f.close()
    except Exception:
        print "Could not erase file:", path


def append_file(path, text):
    try:
        f = open(path, "a+")
        f.write(text)
        f.close()
    except Exception:
        print "Could not append to file:", path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", "-d",
                        help="The directory to write files to.", type=str, default=FOLDER)
    parser.add_argument("--interval", "-i",
                        help="The recording interval time in seconds. Defaults to 1 second.", type=float, default=1)
    args = parser.parse_args()
    daemon(args.directory, args.interval)
