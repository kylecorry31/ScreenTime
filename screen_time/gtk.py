#!/usr/bin/python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


PRIMARY_COLOR = "#48b9c7"
INACTIVE_COLOR = "#E6E6E6"
LABEL_COLOR = "#888888"
LINE_COLOR = "#574f4a"
BACKGROUND_COLOR = "#f5f5f5"


def create_title(title):
    label = Gtk.Label(title)
    label.set_line_wrap(True)
    label.set_halign(Gtk.Align.START)
    label.set_justify(Gtk.Justification.FILL)
    label.set_hexpand(True)
    Gtk.StyleContext.add_class(label.get_style_context(), "h1")
    return label

def create_usage_detail(title, content):
    label = Gtk.Label("{}: {}".format(title, content))
    label.set_line_wrap(True)
    label.set_halign(Gtk.Align.START)
    label.set_justify(Gtk.Justification.FILL)
    label.set_hexpand(True)
    Gtk.StyleContext.add_class(label.get_style_context(), "h2")
    return label


def set_default_margins(box):
    box.set_margin_top(24)
    box.set_margin_bottom(12)
    box.set_margin_left(12)
    box.set_margin_right(12)
