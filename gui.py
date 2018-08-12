#!/usr/bin/python3

from gi.repository import Gtk

from matplotlib.figure import Figure
from numpy import arange, pi, random, linspace
import matplotlib.cm as cm
import matplotlib.pyplot as plt
#Possibly this rendering backend is broken currently
#from matplotlib.backends.backend_gtk3agg import FigureCanvasGTK3Agg as FigureCanvas
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas

window = Gtk.Window()
window.connect("delete-event", Gtk.main_quit)
window.set_default_size(1024, 768)

fig, ax = plt.subplots(figsize=(5,5), dpi=100)

week_days = ['S', 'M', 'T', 'W', 'T', 'F', 'S']
times = [120, 0, 18, 8, 76, 12, 2]

plt.bar(range(len(week_days)), times)
plt.xticks(range(len(week_days)), week_days)

[i.set_linewidth(0) for i in ax.spines.values()]
ax.spines.get('bottom').set_linewidth(0.5)

ax.get_yaxis().set_visible(False)


plt.plot()


sw = Gtk.ScrolledWindow()
window.add(sw)

canvas = FigureCanvas(fig)
canvas.set_size_request(1024, 768)
sw.add_with_viewport(canvas)

window.show_all()
Gtk.main()