BIN_PREFIX = screen-time-daemon

INSTALLNAME = screen_time

.PHONY: install uninstall

install:
	install -D "$(BIN_PREFIX).service" "/etc/systemd/system/$(BIN_PREFIX).service"
	systemctl enable $(BIN_PREFIX).service
	pip3 install . --upgrade

uninstall:
	rm -f /etc/systemd/system/$(BIN_PREFIX).service
	systemctl disable $(BIN_PREFIX).service
	pip3 uninstall .