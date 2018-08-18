BIN_PREFIX = screen-time-daemon

INSTALLNAME = screen_time

.PHONY: all install uninstall clean zip-file

all: screen_time/ setup.py screen-time-daemon.py screen-time-daemon.service data/
	rm -rf _build
	mkdir -p _build
	cp -r $^ _build

clean:
	rm -rf _build

install: all
	cd _build
	install -D "$(BIN_PREFIX).py" "/usr/bin/$(BIN_PREFIX)"
	install -D "$(BIN_PREFIX).service" "/etc/systemd/system/$(BIN_PREFIX).service"
	systemctl enable $(BIN_PREFIX).service
	pip3 install . --upgrade
	cp -r data/screen_time.desktop /usr/share/applications/
	cp -r data/screen_time.png /usr/share/icons/

uninstall: all
	cd _build
	rm -f /usr/bin/$(BIN_PREFIX)
	rm -f /etc/systemd/system/$(BIN_PREFIX).service
	systemctl disable $(BIN_PREFIX).service
	pip3 uninstall .
	rm /usr/share/applications/screen_time.desktop
	rm /usr/share/icons/screen_time.png

zip-file: all
	cd _build && zip -qr "../$(INSTALLNAME)-$(VSTRING).zip" .