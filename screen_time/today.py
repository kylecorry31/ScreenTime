#!/usr/bin/python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas
from .usage import TodayUsage, format_time
import numpy as np
from .gtk import *


class Today(Gtk.Box):

    def __init__(self, parent):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=6)

        set_default_margins(self)
        self.background_color = INACTIVE_COLOR
        self.bar_color = PRIMARY_COLOR

        self.parent = parent

        today_label = create_title("Today")
        self.add(today_label)

        usage = TodayUsage()

        time_label = create_usage_detail("Screen time", format_time(usage.get_total_time()))
        self.add(time_label)

        longest_session_label = create_usage_detail("Longest session",
                                                    format_time(max([d.get_length() for d in usage.sessions])))
        self.add(longest_session_label)

        unlocks_label = create_usage_detail("Unlocks", usage.get_unlocks())
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
        ax.tick_params(axis='x', colors=LABEL_COLOR)
        plt.xticks(range(0, 24 * 60 + 1, 60 * 3), ["12A", "3A", "6A", "9A", "12P", "3P", "6P", "9P", "12A"])
        ax.set_facecolor(BACKGROUND_COLOR)
        fig.set_facecolor(BACKGROUND_COLOR)
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
                d.append(durations[i + 1].start() - durations[i].end())

        d.append(60 * 24 - durations[-1].end())
        return d

    return [60 * 24]
