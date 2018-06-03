#include "usage_reader.h"

int main(){
	long delay = 1;

	unsigned long screen_time_seconds = 0;
	unsigned long unlocks = 1;

	// Load from file
	char* file_contents = read_str(TODAY_FILE);
	if(file_contents){
		sscanf(file_contents, "%ld\n%ld", &screen_time_seconds, &unlocks);
		free(file_contents);
	}

	unsigned long minutes = seconds_to_minutes(screen_time_seconds);
	unsigned long hours = minutes_to_hours(minutes);
	minutes %= 60;

	printf("%ld hr %ld min - %ld unlocks\n", hours, minutes, unlocks);
	return 0;
}