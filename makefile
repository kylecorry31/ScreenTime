install:
	pip3 install .
	cp data/screen_time.desktop /usr/share/applications/
	cp data/screen_time.png /usr/share/icons/

uninstall:
	pip3 uninstall .
	rm /usr/share/applications/screen_time.desktop
	rm /usr/share/icons/screen_time.png

update:
	pip3 install . --upgrade
	cp data/screen_time.desktop /usr/share/applications/
	cp data/screen_time.png /usr/share/icons/
