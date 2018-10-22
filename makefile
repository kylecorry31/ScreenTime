.PHONY: all clean install uninstall update

all:
	$(MAKE) -C daemon clean

install:
	$(MAKE) install -C daemon
	pip3 install .
	cp data/screen_time.desktop ~/.local/share/applications/
	cp data/screen_time.png ~/.local/share/icons/

uninstall:
	$(MAKE) uninstall -C daemon
	pip3 uninstall .
	rm ~/.local/share/applications/screen_time.desktop
	rm ~/.local/share/icons/screen_time.png

update:
	$(MAKE) install -C daemon
	pip3 install . --upgrade
	cp data/screen_time.desktop ~/.local/share/applications/
	cp data/screen_time.png ~/.local/share/icons/


clean:
	$(MAKE) clean -C daemon
