#!/usr/bin/python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from .usage import WeekUsage, format_time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas
from .gtk import *


class Week(Gtk.Box):

    def __init__(self, parent):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=6)

        set_default_margins(self)

        self.bar_color = PRIMARY_COLOR

        self.parent = parent

        week_label = create_title("Last 7 Days")
        self.add(week_label)

        self.time_label = None
        self.average_label = None
        self.unlocks_label = None
        self.daily_unlocks_label = None
        self.chart = None

        self.add_data()

    def refresh(self):
        self.clear_data()
        self.add_data()
        self.show_all()

    def clear_data(self):
        if self.time_label:
            self.remove(self.time_label)
            self.time_label = None

        if self.average_label:
            self.remove(self.average_label)
            self.average_label = None

        if self.unlocks_label:
            self.remove(self.unlocks_label)
            self.unlocks_label = None

        if self.daily_unlocks_label:
            self.remove(self.daily_unlocks_label)
            self.daily_unlocks_label = None

        if self.chart:
            self.remove(self.chart)
            self.chart = None

    def add_data(self):
        try:
            usage = WeekUsage()
        except Exception:
            self.parent.add(create_error_bar("Could not read screen time log"))
            return

        total_time = sum([d.total_time for d in usage.days])
        total_unlocks = sum([d.unlocks for d in usage.days])

        self.time_label = create_usage_detail("Screen time", format_time(total_time))
        self.add(self.time_label)

        self.average_label = create_usage_detail("Daily average", format_time(total_time / 7))
        self.add(self.average_label)

        self.unlocks_label = create_usage_detail("Unlocks", total_unlocks)
        self.add(self.unlocks_label)

        self.daily_unlocks_label = create_usage_detail("Daily unlocks", int(total_unlocks / 7))
        self.add(self.daily_unlocks_label)

        fig, ax = plt.subplots()

        week_days = [get_day_letter(d.date.weekday()) for d in usage.days]

        times = [d.total_time for d in usage.days]

        bars = plt.bar(range(len(times)), times, color=self.bar_color)
        add_labels(ax, bars)
        plt.xticks(range(len(week_days)), week_days)

        [i.set_linewidth(0) for i in ax.spines.values()]
        ax.spines.get('bottom').set_linewidth(0.2)

        ax.get_yaxis().set_visible(False)
        ax.get_xaxis().set_visible(True)
        ax.tick_params(axis='x', colors=LABEL_COLOR)
        ax.set_facecolor(BACKGROUND_COLOR)
        fig.set_facecolor(BACKGROUND_COLOR)
        plt.subplots_adjust(left=0.02, right=0.98)

        plt.axhline(total_time / 7, color=LINE_COLOR, linestyle='dashed', linewidth=0.5)

        plt.plot()

        self.chart = FigureCanvas(fig)
        self.chart.set_size_request(768, 200)
        self.add(self.chart)


def get_day_letter(day):
    if day == 0:
        return 'M'
    elif day == 1:
        return 'T'
    elif day == 2:
        return 'W'
    elif day == 3:
        return 'T'
    elif day == 4:
        return 'F'
    elif day == 5:
        return 'S'
    else:
        return 'S'


def add_labels(ax, rects, xpos='center'):
    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.01 * height,
                format_time(height), ha=ha[xpos], va='bottom', color=LABEL_COLOR)
