all: usage usage_reader

usage_reader: usage_reader.o file_reader.o time_utils.o
	gcc -Wall usage_reader.o file_reader.o time_utils.o -o usage_reader

usage: usage.o file_reader.o time_utils.o
	gcc -Wall usage.o file_reader.o time_utils.o -o usage

usage_reader.o: usage_reader.c *.h

usage.o: usage.c *.h
	gcc -c -Wall usage.c

file_reader.o: file_reader.c file_reader.h
	gcc -c -Wall file_reader.c

time_utils.o: time_utils.c time_utils.h
	gcc -c -Wall time_utils.c