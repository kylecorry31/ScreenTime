BIN_PREFIX = screen-time-daemon

install:
	install -D "$(BIN_PREFIX).py" "/usr/bin/$(BIN_PREFIX)"
	install -D "$(BIN_PREFIX).service" "/etc/systemd/system/$(BIN_PREFIX).service"
	systemctl enable $(BIN_PREFIX).service
	pip3 install .
	cp data/screen_time.desktop /usr/share/applications/
	cp data/screen_time.png /usr/share/icons/

uninstall:
	rm -f /usr/bin/$(BIN_PREFIX)
	rm -f /etc/systemd/system/$(BIN_PREFIX).service
	systemctl disable $(BIN_PREFIX).service
	pip3 uninstall .
	rm /usr/share/applications/screen_time.desktop
	rm /usr/share/icons/screen_time.png
