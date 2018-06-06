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
	char* folder = "st/";
	if (argc == 3)
	{
		folder = argv[2];
	}

	long delay = 1;

	m_sleep(delay);

	char* today_file = create_file_path(folder, "week.txt");

	FILE * fp = fopen(today_file, "r");
	time_t last_updated = time(NULL);
	if(fp){
		time_t file_time;
		fscanf(fp, "%ld", &file_time);
		fclose(fp);
		if (!on_same_week(localtime(&last_updated), localtime(&file_time)))
		{
			char* archive_file = create_file_path(folder, "last-week.txt");
			copy_file(today_file, archive_file);
			remove(today_file);
			free(archive_file);
		}
	}


	while(1){

		fp = fopen(today_file, "a");

		time_t current_time = time(NULL);

		fprintf(fp, "%ld\n", current_time);

		fclose(fp);

		if(!on_same_week(localtime(&last_updated), localtime(&current_time))){
			char* archive_file = create_file_path(folder, "last-week.txt");
			copy_file(today_file, archive_file);
			remove(today_file);
			free(archive_file);
		}
		
		// Delay
		m_sleep(delay);
	}

	free(today_file);

}

/**
 * Print the usage.
 * 
 * @param argc The argc from the command line.
 * @param argv The argv from the command line.
 */
void print_usage(int argc, char* argv[]){
	char* folder = "st/";
	if (argc == 3)
	{
		folder = argv[2];
	}

	long delay = 1;

	char* today_file = create_file_path(folder, "week.txt");

	FILE* fp = fopen(today_file, "r");

	if(!fp){
		printf("Error reading file.");
		return;
	}

	time_t date;

	struct tm today = *get_time();

	unsigned long sot = 0;


	while(fscanf(fp, "%ld\n", &date) == 1) {
		if (on_same_date(&today, localtime(&date)))
		{
			sot += delay;
		}
	}

	fclose(fp);

	unsigned long minutes = seconds_to_minutes(sot);
	unsigned long hours = minutes_to_hours(minutes);
	minutes %= 60;

	if (hours == 0)
	{
		printf("%ldm\n", minutes);
	} else {
		printf("%ldh %ldm\n", hours, minutes);
	}
}