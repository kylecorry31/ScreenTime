#include "usage_utils.h"

usage_t make_usage(unsigned long screen_time_sec, unsigned int unlocks, unsigned long last_updated){
	usage_t usage;
	usage.screen_time_sec = screen_time_sec;
	usage.unlocks = unlocks;
	usage.last_updated = last_updated;
	return usage;
}

usage_t get_current_usage(char* filename){
	usage_t usage = make_usage(0, 0, 0);
	char* file_contents = read_str(filename);
	if(file_contents){
		sscanf(file_contents, "%ld\n%d\n%ld", &(usage.screen_time_sec), &(usage.unlocks), &(usage.last_updated));
		free(file_contents);
	}
	return usage;
}

void set_current_usage(char* filename, usage_t usage){
	int length = snprintf(NULL, 0, "%ld\n%d\n%ld", usage.screen_time_sec, usage.unlocks, usage.last_updated);
	char* str = malloc(sizeof(char) * (length + 1));
	snprintf(str, length + 1, "%ld\n%d\n%ld", usage.screen_time_sec, usage.unlocks, usage.last_updated);
	write_str(filename, str);
	free(str);
}