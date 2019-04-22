#!/usr/bin/python3
'''
   Copyright 2017 Mirko Brombin (brombinmirko@gmail.com)
   Copyright 2017 Ian Santopietro (ian@system76.com)
   Copyright 2018 Kyle Corry (kylecorry31@gmail.com)
'''

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio


class Headerbar(Gtk.HeaderBar):

    def __init__(self, parent):
        Gtk.HeaderBar.__init__(self)
        self.parent = parent

        self.set_show_close_button(True)
        self.set_has_subtitle(False)

        self.switcher = Gtk.StackSwitcher()
        self.switcher.set_baseline_position(Gtk.BaselinePosition.CENTER)
        self.set_custom_title(self.switcher)

        # spinner
        self.spinner = Gtk.Spinner()
        self.pack_end(self.spinner)

        # Refresh button
        self.refresh_button = Gtk.Button()
        refresh_icon = Gio.ThemedIcon(name="view-refresh-symbolic")
        image = Gtk.Image.new_from_gicon(refresh_icon, Gtk.IconSize.BUTTON)
        self.refresh_button.add(image)
        self.pack_end(self.refresh_button)
        self.refresh_button.connect("clicked", self.parent.refresh)
