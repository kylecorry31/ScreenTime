#!/usr/bin/python3
from .config import read_config, write_config, create_default_config


def get_break_points_goal():
    cfg = read_config()
    return cfg['goals']['break_points']


def set_break_points_goal(goal):
    cfg = read_config()
    cfg['goals']['break_points'] = goal
    write_config(cfg)


def get_screen_off_points_goal():
    cfg = read_config()
    return cfg['goals']['screen_off_points']


def set_screen_off_points_goal(goal):
    cfg = read_config()
    cfg['goals']['screen_off_points'] = goal
    write_config(cfg)


def break_points(current_time, session_lengths):
    return int(current_time * 2 - sum([int(x * 2) for x in session_lengths]))


def screen_off_points(current_time, screen_on_time):
    return int((current_time - screen_on_time) * 4)
