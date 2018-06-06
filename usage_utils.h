#ifndef USAGE_UTILS_H
#define USAGE_UTILS_H

#include "file_reader.h"
#include "time_utils.h"
#include <stdio.h>
#include <time.h>

typedef struct usage usage_t;
typedef struct session session_t;

struct usage {
	unsigned long screen_time_sec;
	unsigned int unlocks;
	time_t last_updated;
	int num_sessions;
	session_t* sessions;
};

struct session {
	time_t start_time;
	time_t end_time;
};

usage_t make_usage(unsigned long screen_time_sec, unsigned int unlocks, time_t last_updated, session_t* sessions, int num_sessions);
usage_t get_current_usage(char* filename);
void set_current_usage(char* filename, usage_t usage);
void add_session(usage_t* usage, session_t session);
void free_usage(usage_t usage);

session_t make_session(time_t start_time, time_t end_time);
long session_length(session_t session);

#endif