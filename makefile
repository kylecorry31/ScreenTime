BIN_PREFIX = usage

all: $(BIN_PREFIX) $(BIN_PREFIX)_reader $(BIN_PREFIX)_tests

install: $(BIN_PREFIX) $(BIN_PREFIX)_reader
	install -D "$(BIN_PREFIX)" "/usr/bin/$(BIN_PREFIX)"
	install -D "$(BIN_PREFIX)_reader" "/usr/bin/$(BIN_PREFIX)_reader"
	install -D "$(BIN_PREFIX)_startup.sh" "/usr/bin/$(BIN_PREFIX)_startup.sh"
	install -D "$(BIN_PREFIX).service" "/etc/systemd/system/$(BIN_PREFIX).service"
	systemctl enable $(BIN_PREFIX).service

uninstall:
	rm -f /usr/bin/$(BIN_PREFIX)
	rm -f /usr/bin/$(BIN_PREFIX)_reader
	rm -f /usr/bin/$(BIN_PREFIX)_startup.sh
	rm -f /etc/systemd/system/$(BIN_PREFIX).service
	systemctl disable $(BIN_PREFIX).service

$(BIN_PREFIX)_reader: usage_reader.o file_reader.o time_utils.o
	gcc -Wall $^ -o $(BIN_PREFIX)_reader

$(BIN_PREFIX): usage.o file_reader.o time_utils.o
	gcc -Wall $^ -o $(BIN_PREFIX)

$(BIN_PREFIX)_tests: usage_tests.o file_reader.o time_utils.o
	gcc -Wall $^ -o $(BIN_PREFIX)_tests

usage_tests.o: usage_tests.c *.h
	gcc -c -Wall usage_tests.c

usage_reader.o: usage_reader.c *.h
	gcc -c -Wall usage_reader.c

usage.o: usage.c *.h
	gcc -c -Wall usage.c

file_reader.o: file_reader.c file_reader.h
	gcc -c -Wall file_reader.c

time_utils.o: time_utils.c time_utils.h
	gcc -c -Wall time_utils.c

clean:
	rm *.o
	rm $(BIN_PREFIX)
	rm $(BIN_PREFIX)_reader
	rm usage_tests