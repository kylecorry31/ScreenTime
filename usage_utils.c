#include "usage_utils.h"

/**
 * Make a usage_t struct.
 * 
 * @param screen_time_sec The screen time in seconds.
 * @param unlocks The number of unlocks.
 * @param last_updated The last time the usage was updated.
 * @return The usage struct.
 */
usage_t make_usage(unsigned long screen_time_sec, unsigned int unlocks, time_t last_updated){
	usage_t usage;
	usage.screen_time_sec = screen_time_sec;
	usage.unlocks = unlocks;
	usage.last_updated = last_updated;
	return usage;
}

/**
 * Get the current usage for the day.
 * 
 * @param filename The file to get the current usage from.
 * @return The current usage.
 */
usage_t get_current_usage(char* filename){
	usage_t usage = make_usage(0, 0, 0);
	char* file_contents = read_str(filename);
	if(file_contents){
		sscanf(file_contents, "%ld\n%d\n%ld", &(usage.screen_time_sec), &(usage.unlocks), &(usage.last_updated));
		free(file_contents);
	}
	return usage;
}

/**
 * Set the current usage for the day.
 * 
 * @param filename The file to save the current usage to.
 * @param usage The current usage.
 */
void set_current_usage(char* filename, usage_t usage){
	int length = snprintf(NULL, 0, "%ld\n%d\n%ld", usage.screen_time_sec, usage.unlocks, usage.last_updated);
	char* str = malloc(sizeof(char) * (length + 1));
	snprintf(str, length + 1, "%ld\n%d\n%ld", usage.screen_time_sec, usage.unlocks, usage.last_updated);
	write_str(filename, str);
	free(str);
}

/**
 * Make a session struct.
 * 
 * @param start_time The start time of the session.
 * @param end_time The end time of the session.
 * 
 * @return The session.
 */
session_t make_session(time_t start_time, time_t end_time){
	session_t session;
	session.start_time = start_time;
	session.end_time = end_time;
	return session;
}

/**
 * Calculates the session length in seconds.
 * 
 * @param session The session.
 * @return The length of the session in seconds.
 */
long session_length(session_t session){
	return session.end_time - session.start_time;
}