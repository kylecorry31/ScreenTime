#include "usage_reader.h"

int main(int argc, char* argv[]){

	char* today_file = "usage.txt";

	if (argc == 2)
	{
		today_file = argv[1];
	}

	long delay = 1;

	unsigned long screen_time_seconds = 0;
	unsigned long unlocks = 1;

	// Load from file
	char* file_contents = read_str(today_file);
	if(file_contents){
		sscanf(file_contents, "%ld\n%ld", &screen_time_seconds, &unlocks);
		free(file_contents);
	}

	unsigned long minutes = seconds_to_minutes(screen_time_seconds);
	unsigned long hours = minutes_to_hours(minutes);
	minutes %= 60;

	printf("%ld hr %ld min\n%ld unlocks\n", hours, minutes, unlocks);
	return 0;
}