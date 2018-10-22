# Modified from https://github.com/pop-os/system76-power/

prefix ?= ~/.local
exec_prefix = $(prefix)
bindir = $(exec_prefix)/bin

.PHONY: all clean install uninstall update

BIN=screen-time

all: target/release/$(BIN)

clean:
	cargo clean

install: all
	install -D -m 04755 "target/release/$(BIN)" $(DESTDIR)$(bindir)/$(BIN)
	install -D "$(BIN)-service.desktop" ~/.config/autostart/$(BIN)-service.desktop

uninstall:
	rm -f $(DESTDIR)$(bindir)/$(BIN)
	rm -f ~/.config/autostart/$(BIN)-service.desktop


update:
	cargo update

target/release/$(BIN): Cargo.lock Cargo.toml src/*.rs
	cargo build --release; \
