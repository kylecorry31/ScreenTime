#include "usage.h"

int main(){

	long delay = 1;

	unsigned long screen_time_seconds = 0;
	unsigned long unlocks = 1;
	m_sleep(delay);

	// Load from file
	char* file_contents = read_str(TODAY_FILE);
	if(file_contents){
		sscanf(file_contents, "%ld\n%ld", &screen_time_seconds, &unlocks);
		free(file_contents);
	}

	struct tm last_time = *get_time();
	while(1){
		struct tm* date = get_time();
		// printf("%d-%d-%d %d:%d:%d\n", date->tm_mon, date->tm_mday, date->tm_year + 1900, 
		// 	date->tm_hour, date->tm_min, date->tm_sec);
		screen_time_seconds += delay;
		if (!on_same_date(&last_time, date))
		{
			screen_time_seconds = 0;
			unlocks = 1;
		} else {
			time_t time_diff = mktime(date) - mktime(&last_time);
			if (time_diff >= (delay + 2))
			{
				unlocks++;
			}
		}
		last_time = *date;

		// Write to a file
		int length = snprintf(NULL, 0, "%ld\n%ld", screen_time_seconds, unlocks);
		char* str = malloc(length + 1);
		snprintf(str, length + 1, "%ld\n%ld", screen_time_seconds, unlocks);
		write_str(TODAY_FILE, str);
		free(str);

		// Delay
		m_sleep(delay);
	}
	return 0;
}

/**
 * Sleep a certain amount of seconds.
 * 
 * @param seconds The number of seconds to sleep for.
 * @return The return code from usleep.
 */
int m_sleep(double seconds){
	return usleep((int) (1000000 * seconds));
}