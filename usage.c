#include "usage.h"

int main(int argc, char* argv[]){

	// TODO: print help

	if (argc == 2 || argc == 3)
	{
		if (strcmp(argv[1], "daemon") == 0)
		{
			daemon_mode(argc, argv);
		}

		if (strcmp(argv[1], "--help") == 0)
		{
			help();
			return 0;
		}
	} 

	if (argc <= 2)
	{
		print_usage(argc, argv);
		return 0;
	}


	help();
	return 1;
}


/**
 * Print the help to see how to use the program.
 */
void help(void){
	printf("screen-time [daemon] [path]\n");
	printf("\tdaemon - run in daemon mode\n");
	printf("\tno arguments - query the current usage\n");
	printf("\tpath - the usage file to read from\n");

	printf("\nExample\n");
	printf("Query the current usage\n");
	printf("\tscreen-time\n");
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


/**
 * Run in daemon mode.
 * 
 * @param argc The argc from the command line.
 * @param argv The argv from the command line.
 */
void daemon_mode(int argc, char* argv[]){
	// Load the today file.
	char* today_file = "/screen-time/usage.txt";
	if (argc == 3)
	{
		today_file = argv[2];
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
	} else {
		usage.unlocks++;
	}

	time_t unlock_time = mktime(&last_time);

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
				session_t session = make_session(unlock_time, mktime(&last_time));
				printf("%ld\n", session_length(session));
				// TODO: save session times
				add_session(&usage, session);
				unlock_time = mktime(date);
			}
		}
		last_time = *date;

		usage.last_updated = mktime(date);
		set_current_usage(today_file, usage);

		// Delay
		m_sleep(delay);
	}
}


/**
 * Print the usage.
 * 
 * @param argc The argc from the command line.
 * @param argv The argv from the command line.
 */
void print_usage(int argc, char* argv[]){
	char* today_file = "/screen-time/usage.txt";

	if (argc == 2)
	{
		today_file = argv[1];
	}

	// Load from file
	usage_t usage = get_current_usage(today_file);

	unsigned long minutes = seconds_to_minutes(usage.screen_time_sec);
	unsigned long hours = minutes_to_hours(minutes);
	minutes %= 60;

	if (hours == 0)
	{
		printf("%ldm\n%d unlocks\n", minutes, usage.unlocks);
	} else {
		printf("%ldh %ldm\n%d unlocks\n", hours, minutes, usage.unlocks);
	}
}