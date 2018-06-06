#include "usage_tests.h"

int main(int argc, char* argv[]){
	test_file_writing();
	test_time();
	printf("All test cases passed.\n");
	return 0;
}


void test_file_writing(void){

	char* FOLDER = "screen-time/";

	char* FILE_NAME = "usage_test.txt";

	char* path = create_file_path(FOLDER, FILE_NAME);
	assert(strcmp(path, "screen-time/usage_test.txt") == 0);
	free(path);

	remove(FILE_NAME);

	// Read when file doesn't exist
	assert(read_str(FILE_NAME) == NULL);

	// Test writing
	write_str(FILE_NAME, "test");
	assert(strlen(read_str(FILE_NAME)) == 4);
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

	// On same week
	struct tm* date = calloc(1, sizeof(struct tm));
	strptime("6/6/18", "%D", date);
	struct tm wednesday = *date;
	strptime("6/7/18", "%D", date);
	struct tm thursday = *date;
	strptime("6/9/18", "%D", date);
	struct tm saturday = *date;
	strptime("6/10/18", "%D", date);
	struct tm sunday = *date;
	strptime("6/10/24", "%D", date);
	struct tm sunday2 = *date;

	free(date);

	assert(on_same_week(&wednesday, &thursday));
	assert(on_same_week(&wednesday, &saturday));
	assert(!on_same_week(&wednesday, &sunday));
	assert(!on_same_week(&sunday, &sunday2));


	printf("Time:\t\t\t[OK]\n");
}