BIN_PREFIX = screen-time-daemon

install:
	install -D "$(BIN_PREFIX).py" "/usr/bin/$(BIN_PREFIX)"
	install -D "$(BIN_PREFIX).service" "/etc/systemd/system/$(BIN_PREFIX).service"
	systemctl enable $(BIN_PREFIX).service
	python3 setup.py install
	cp data/screen_time.desktop /usr/share/applications/
	cp data/screen_time.png /usr/share/icons/

uninstall:
	rm -f /usr/bin/$(BIN_PREFIX)
	rm -f /etc/systemd/system/$(BIN_PREFIX).service
	systemctl disable $(BIN_PREFIX).service
