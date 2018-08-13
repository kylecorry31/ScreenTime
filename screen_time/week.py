#!/usr/bin/python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Week(Gtk.Box):

    def __init__(self, parent):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.set_margin_top(24)
        self.set_margin_bottom(12)
        self.set_margin_left(12)
        self.set_margin_right(12)

        self.parent = parent

        week_label = Gtk.Label("Last 7 Day's Screen Time")
        week_label.set_line_wrap(True)
        week_label.set_halign(Gtk.Align.START)
        week_label.set_justify(Gtk.Justification.FILL)
        week_label.set_hexpand(True)
        Gtk.StyleContext.add_class(week_label.get_style_context(), "h1")

        self.add(week_label)
