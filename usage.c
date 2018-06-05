#include "usage.h"

int main(int argc, char* argv[]){

	char* today_file = "/tmp/usage/usage.txt";

	if (argc == 2)
	{
		today_file = argv[1];
	}

	long delay = 1;

	m_sleep(delay);

	struct tm last_time = *get_time();

	// Load from file

	usage_t usage = get_current_usage(today_file);
	if (!on_same_date(&last_time, localtime(&(usage.last_updated))))
	{
		usage.unlocks = 1;
		usage.screen_time_sec = 0;
	}

	while(1){
		struct tm* date = get_time();
		// printf("%d-%d-%d %d:%d:%d\n", date->tm_mon, date->tm_mday, date->tm_year + 1900, 
		// 	date->tm_hour, date->tm_min, date->tm_sec);
		usage.screen_time_sec += delay;
		if (!on_same_date(&last_time, date))
		{
			// TODO: archive
			usage.screen_time_sec = 0;
			usage.unlocks = 1;
		} else {
			time_t time_diff = mktime(date) - mktime(&last_time);
			if (time_diff >= (delay + 2))
			{
				usage.unlocks++;
			}
		}
		last_time = *date;

		usage.last_updated = mktime(date);
		set_current_usage(today_file, usage);

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