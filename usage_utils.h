#ifndef USAGE_UTILS_H
#define USAGE_UTILS_H

#include "file_reader.h"
#include <stdio.h>

typedef struct usage usage_t;

struct usage {
	unsigned long screen_time_sec;
	unsigned int unlocks;
	unsigned long last_updated;
};

usage_t make_usage(unsigned long screen_time_sec, unsigned int unlocks, unsigned long last_updated);
usage_t get_current_usage(char* filename);
void set_current_usage(char* filename, usage_t usage);

#endif