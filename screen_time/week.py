#!/usr/bin/python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from .usage import WeekUsage, format_time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas


class Week(Gtk.Box):

    def __init__(self, parent):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.set_margin_top(24)
        self.set_margin_bottom(12)
        self.set_margin_left(12)
        self.set_margin_right(12)

        self.bar_color = '#027cf7'

        self.parent = parent

        week_label = Gtk.Label("Last 7 Day's Screen Time")
        week_label.set_line_wrap(True)
        week_label.set_halign(Gtk.Align.START)
        week_label.set_justify(Gtk.Justification.FILL)
        week_label.set_hexpand(True)
        Gtk.StyleContext.add_class(week_label.get_style_context(), "h1")

        self.add(week_label)

        usage = WeekUsage()

        total_time = sum([d.total_time for d in usage.days])
        total_unlocks = sum([d.unlocks for d in usage.days])

        time_label = Gtk.Label("Total time: {}".format(format_time(total_time)))
        time_label.set_line_wrap(True)
        time_label.set_halign(Gtk.Align.START)
        time_label.set_justify(Gtk.Justification.FILL)
        time_label.set_hexpand(True)
        Gtk.StyleContext.add_class(time_label.get_style_context(), "h2")

        self.add(time_label)

        unlocks_label = Gtk.Label("Unlocks: {}".format(total_unlocks))
        unlocks_label.set_line_wrap(True)
        unlocks_label.set_halign(Gtk.Align.START)
        unlocks_label.set_justify(Gtk.Justification.FILL)
        unlocks_label.set_hexpand(True)
        Gtk.StyleContext.add_class(unlocks_label.get_style_context(), "h2")

        self.add(unlocks_label)

        fig, ax = plt.subplots()

        week_days = [get_day_letter(d.date.weekday()) for d in usage.days]

        times = [int(d.total_time / 60) for d in usage.days]

        bars = plt.bar(range(len(times)), times, color=self.bar_color)
        add_labels(ax, bars)
        plt.xticks(range(len(week_days)), week_days)

        [i.set_linewidth(0) for i in ax.spines.values()]
        ax.spines.get('bottom').set_linewidth(0.5)

        ax.get_yaxis().set_visible(False)
        ax.get_xaxis().set_visible(True)
        ax.tick_params(axis='x', colors='#555555')
        ax.set_facecolor("#f5f5f5")
        fig.set_facecolor('#f5f5f5')
        plt.subplots_adjust(left=0.02, right=0.98)

        plt.plot()

        canvas = FigureCanvas(fig)
        canvas.set_size_request(768, 200)
        self.add(canvas)


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
                format_time(height * 60), ha=ha[xpos], va='bottom', color="#555555")
