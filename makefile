BIN_PREFIX = screen-time-daemon

install:
	install -D "$(BIN_PREFIX).py" "/usr/bin/$(BIN_PREFIX)"
	install -D "$(BIN_PREFIX).service" "/etc/systemd/system/$(BIN_PREFIX).service"
	systemctl enable $(BIN_PREFIX).service

uninstall:
	rm -f /usr/bin/$(BIN_PREFIX)
	rm -f /etc/systemd/system/$(BIN_PREFIX).service
	systemctl disable $(BIN_PREFIX).service
