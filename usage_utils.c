#include "usage_utils.h"

/**
 * Make a usage_t struct.
 * 
 * @param screen_time_sec The screen time in seconds.
 * @param unlocks The number of unlocks.
 * @param last_updated The last time the usage was updated.
 * @param sessions The sessions.
 * @param num_sessions The number of sessions.
 * @return The usage struct.
 */
usage_t make_usage(unsigned long screen_time_sec, unsigned int unlocks, time_t last_updated, session_t* sessions, int num_sessions){
	usage_t usage;
	usage.screen_time_sec = screen_time_sec;
	usage.unlocks = unlocks;
	usage.last_updated = last_updated;
	usage.sessions = sessions;
	usage.num_sessions = num_sessions;
	return usage;
}

/**
 * Adds a session to the usage struct.
 * 
 * @param usage The usage.
 * @param session The session.
 */
void add_session(usage_t* usage, session_t session){
	int length = usage->num_sessions;
	if (length == 0)
	{	
		usage->sessions = malloc(sizeof(session_t));
		usage->sessions[0] = session;
		usage->num_sessions++;
	} else {
		// Create a new array
		session_t* sessions = malloc(sizeof(session_t) * (length + 1));
		// Copy the old array
		for (int i = 0; i < length; ++i)
		{
			sessions[i] = usage->sessions[i];
		}
		sessions[length] = session;
		// Free the old array
		free(usage->sessions);
		// Replace the old array
		usage->sessions = sessions;
		usage->num_sessions++;
	}
}


/**
 * Free the usage struct.
 * 
 * @param usage The usage.
 */
void free_usage(usage_t usage){
	if(usage.sessions){
		free(usage.sessions);
		usage.num_sessions = 0;
	}
}

/**
 * Get the current usage for the day.
 * 
 * @param filename The file to get the current usage from.
 * @return The current usage.
 */
usage_t get_current_usage(char* filename){
	usage_t usage = make_usage(0, 0, 0, 0, 0);
	char* file_contents = read_str(filename);
	if(file_contents){
		// TODO: load sessions
		sscanf(file_contents, "%ld\nTotal: %ld\nUnlocks: %d", &(usage.last_updated), &(usage.screen_time_sec), &(usage.unlocks));
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
	// int length = snprintf(NULL, 0, "%ld\n%d\n%ld", usage.screen_time_sec, usage.unlocks, usage.last_updated);
	// char* str = malloc(sizeof(char) * (length + 1));
	// snprintf(str, length + 1, "%ld\n%d\n%ld", usage.screen_time_sec, usage.unlocks, usage.last_updated);
	// write_str(filename, str);

	FILE* fp = fopen(filename, "w+");
	// struct tm* date = localtime(&(usage.last_updated));
	fprintf(fp, "%ld\n", usage.last_updated);
	// fprintf(fp, "%d-%d-%d\n", date->tm_mon, date->tm_mday, date->tm_year + 1900);
	fprintf(fp, "Total: %ld\n", usage.screen_time_sec);
	fprintf(fp, "Unlocks: %d\n", usage.unlocks);
	fprintf(fp, "Times: ");
	for (int i = 0; i < usage.num_sessions; i++)
	{

		session_t session = usage.sessions[i];
		time_t start = session.start_time;
		time_t end = session.end_time;
		struct tm start_time = *localtime(&start);
		struct tm end_time = *localtime(&end);

		fprintf(fp, "%d:%d-%d:%d", start_time.tm_hour, start_time.tm_min, end_time.tm_hour, end_time.tm_min);
		if (i != usage.num_sessions - 1)
		{
			fprintf(fp, ", ");
		}
	}
	fprintf(fp, "\n");
	fclose(fp);
	// free(str);
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