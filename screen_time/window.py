#!/usr/bin/python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib
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
        self.css_provider = Gtk.CssProvider()
        # try:
        #     self.css_provider.load_from_path('data/style.css')
        # except GLib.Error:
        #     self.css_provider.load_from_path('/usr/share/screen_time/style.css')
        self.context = Gtk.StyleContext()
        self.context.add_provider_for_screen(self.screen, self.css_provider,
                                             Gtk.STYLE_PROVIDER_PRIORITY_USER)
