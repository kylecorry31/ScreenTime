#!/usr/bin/python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas
from .usage import TodayUsage, format_time
import numpy as np


class Today(Gtk.Box):

    def __init__(self, parent):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.set_margin_top(24)
        self.set_margin_bottom(12)
        self.set_margin_left(12)
        self.set_margin_right(12)
        self.background_color = '#eeeeee'
        self.bar_color = '#027cf7'

        self.parent = parent

        today_label = Gtk.Label("Today's Screen Time")
        today_label.set_line_wrap(True)
        today_label.set_halign(Gtk.Align.START)
        today_label.set_justify(Gtk.Justification.FILL)
        today_label.set_hexpand(True)
        Gtk.StyleContext.add_class(today_label.get_style_context(), "h1")

        self.add(today_label)

        usage = TodayUsage()

        time_label = Gtk.Label("Total time: {}".format(format_time(usage.get_total_time())))
        time_label.set_line_wrap(True)
        time_label.set_halign(Gtk.Align.START)
        time_label.set_justify(Gtk.Justification.FILL)
        time_label.set_hexpand(True)
        Gtk.StyleContext.add_class(time_label.get_style_context(), "h2")

        self.add(time_label)

        unlocks_label = Gtk.Label("Unlocks: {}".format(usage.get_unlocks()))
        unlocks_label.set_line_wrap(True)
        unlocks_label.set_halign(Gtk.Align.START)
        unlocks_label.set_justify(Gtk.Justification.FILL)
        unlocks_label.set_hexpand(True)
        Gtk.StyleContext.add_class(unlocks_label.get_style_context(), "h2")

        self.add(unlocks_label)

        fig, ax = plt.subplots()

        times = get_chart_times(usage.sessions)

        last = []

        on = False

        plt.xlim(xmax=60 * 24)

        index = [1]

        for t in times:

            color = self.bar_color if on else self.background_color

            item = np.array([t])

            if len(last):
                plt.barh(index, item, left=sum(last), color=color, edgecolor=color, linewidth=0)
            else:
                plt.barh(index, item, color=color, edgecolor=color, linewidth=0)
            last.append(item)

            on = not on

        [i.set_linewidth(0) for i in ax.spines.values()]

        ax.get_yaxis().set_visible(False)
        ax.get_xaxis().set_visible(True)
        ax.tick_params(axis='x', colors='#555555')
        plt.xticks(range(0, 24*60, 60 * 6), ["12A", "6A", "12P", "6P"])
        ax.set_facecolor("#f5f5f5")
        fig.set_facecolor('#f5f5f5')
        plt.subplots_adjust(left=0.02, right=0.98)

        plt.plot()

        canvas = FigureCanvas(fig)
        canvas.set_size_request(768, 200)

        self.add(canvas)


def get_chart_times(durations):
    d = []
    if len(durations):
        d.append(durations[0].start())

        for i in range(len(durations)):
            # Append session
            d.append(durations[i].end() - durations[i].start())

            # Append break
            if i != len(durations) - 1:
                d.append(durations[i+1].start() - durations[i].end())

        d.append(60*24 - durations[-1].end())
        return d

    return [60 * 24]