BIN_PREFIX = screen-time

install: $(BIN_PREFIX)
	install -D "$(BIN_PREFIX).py" "/usr/bin/$(BIN_PREFIX)"
	install -D "$(BIN_PREFIX)_startup.sh" "/usr/bin/$(BIN_PREFIX)_startup.sh"
	install -D "$(BIN_PREFIX).service" "/etc/systemd/system/$(BIN_PREFIX).service"
	systemctl enable $(BIN_PREFIX).service

uninstall:
	rm -f /usr/bin/$(BIN_PREFIX)
	rm -f /usr/bin/$(BIN_PREFIX)_startup.sh
	rm -f /etc/systemd/system/$(BIN_PREFIX).service
	systemctl disable $(BIN_PREFIX).service