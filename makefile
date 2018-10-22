install:
	pip3 install .
	cp data/screen_time.desktop ~/.local/share/applications/
	cp data/screen_time.png ~/.local/share/icons/

uninstall:
	pip3 uninstall .
	rm ~/.local/share/applications/screen_time.desktop
	rm ~/.local/share/icons/screen_time.png

update:
	pip3 install . --upgrade
	cp data/screen_time.desktop ~/.local/share/applications/
	cp data/screen_time.png ~/.local/share/icons/
