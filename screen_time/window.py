#!/usr/bin/python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from .stack import Stack
from .headerbar import Headerbar

class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)

        self.hbar = Headerbar(self)
        self.set_titlebar(self.hbar)

        self.stack = Stack(self)
        self.add(self.stack)

        self.hbar.switcher.set_stack(self.stack.stack)

        self.screen = Gdk.Screen.get_default()

    def refresh(self, _):
        self.stack.refresh()
