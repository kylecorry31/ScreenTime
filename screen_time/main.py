#!/usr/bin/python3

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from .window import Window


class Application(Gtk.Application):

    def do_activate(self):
        self.win = Window()
        self.win.set_title("Screen Time")
        self.win.set_default_size(768, 480)
        self.win.connect("delete-event", Gtk.main_quit)
        self.win.show_all()

        Gtk.main()


app = Application()

style_provider = Gtk.CssProvider()
Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(), style_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)

app.run()
