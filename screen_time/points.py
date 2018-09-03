#!/usr/bin/python3


def break_points(current_time, session_lengths):
    return int(current_time * 2 - sum([int(x * 2) for x in session_lengths]))


def screen_off_points(current_time, screen_on_time):
    return int((current_time - screen_on_time) * 4)
