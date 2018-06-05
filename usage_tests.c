#include "usage_tests.h"

int main(int argc, char* argv[]){
	test_file_writing();
	test_time();
	test_usage();
	printf("All test cases passed.\n");
	return 0;
}


void test_file_writing(void){
	char* FILE_NAME = "usage_test.txt";
	remove(FILE_NAME);

	// Read when file doesn't exist
	assert(read_str(FILE_NAME) == NULL);

	// Test writing
	write_str(FILE_NAME, "test");
	assert(strcmp(read_str(FILE_NAME), "test") == 0);

	// Test overwriting
	write_str(FILE_NAME, "hello");
	assert(strcmp(read_str(FILE_NAME), "hello") == 0);

	// Test writing empty string
	write_str(FILE_NAME, "");
	assert(strcmp(read_str(FILE_NAME), "") == 0);

	remove(FILE_NAME);
	printf("File writing:\t\t[OK]\n");
}

void test_time(void){

	// Seconds to minutes
	assert(seconds_to_minutes(0) == 0);
	assert(seconds_to_minutes(30) == 0);
	assert(seconds_to_minutes(60) == 1);
	assert(seconds_to_minutes(130) == 2);

	// Minutes to hours
	assert(minutes_to_hours(0) == 0);
	assert(minutes_to_hours(30) == 0);
	assert(minutes_to_hours(60) == 1);
	assert(minutes_to_hours(130) == 2);

	// On same date
	struct tm * current_time = get_time();
	assert(current_time != NULL);

	struct tm time1 = *current_time;
	struct tm time2 = *current_time;

	assert(on_same_date(&time1, &time2));

	time1.tm_mday++;
	assert(!on_same_date(&time1, &time2));

	time1.tm_mday--;
	time1.tm_year++;
	assert(!on_same_date(&time1, &time2));

	time1.tm_year--;
	time1.tm_mon++;
	assert(!on_same_date(&time1, &time2));

	time1.tm_mon--;
	time1.tm_min++;
	assert(on_same_date(&time1, &time2));

	time1.tm_hour++;
	assert(on_same_date(&time1, &time2));

	printf("Time:\t\t\t[OK]\n");
}


void test_usage(void){
	// Make usage
	usage_t usage = make_usage(2, 1, 0, NULL, 0);
	assert(usage.screen_time_sec == 2);
	assert(usage.unlocks == 1);
	assert(usage.last_updated == 0);

	// Set and get usage
	char* FILE_NAME = "usage_test.txt";
	remove(FILE_NAME);

	usage = get_current_usage(FILE_NAME);
	assert(usage.screen_time_sec == 0);
	assert(usage.unlocks == 0);
	assert(usage.last_updated == 0);


	set_current_usage(FILE_NAME, make_usage(2, 1, 0, NULL, 0));

	usage = get_current_usage(FILE_NAME);
	assert(usage.screen_time_sec == 2);
	assert(usage.unlocks == 1);
	assert(usage.last_updated == 0);

	remove(FILE_NAME);

	// Sessions
	assert(usage.sessions == NULL);
	assert(usage.num_sessions == 0);

	session_t session = make_session(0, 1);

	assert(session_length(session) == 1);

	add_session(&usage, session);

	assert(usage.num_sessions == 1);
	assert(usage.sessions != NULL);
	assert(usage.sessions[0].start_time == session.start_time);
	assert(usage.sessions[0].end_time == session.end_time);

	session_t session2 = make_session(100, 150);

	assert(session_length(session2) == 50);

	add_session(&usage, session2);

	assert(usage.num_sessions == 2);
	assert(usage.sessions != NULL);
	assert(usage.sessions[0].start_time == session.start_time);
	assert(usage.sessions[0].end_time == session.end_time);
	assert(usage.sessions[1].start_time == session2.start_time);
	assert(usage.sessions[1].end_time == session2.end_time);

	free_usage(usage);

	printf("Usage:\t\t\t[OK]\n");
}