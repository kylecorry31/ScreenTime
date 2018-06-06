#include "time_utils.h"

/**
 * Get the current time.
 * 
 * @return The current time.
 */
struct tm * get_time(void){
	time_t timer = time(NULL);
	return localtime(&timer);
}

/**
 *
 * @param time1 The first time.
 * @param time2 The second time.
 * @return 1 if the two times are on the same date, 0 otherwise.
 */
int on_same_date(struct tm * time1, struct tm * time2){
	return time1->tm_mday == time2->tm_mday &&
			time1->tm_mon == time2->tm_mon &&
			time1->tm_year == time2->tm_year;
}

int on_same_week(struct tm * time1, struct tm * time2){
	// TODO: check this
	if (on_same_date(time1, time2))
	{
		return 1;
	}


	int week_day1 = time1->tm_wday;

	int year_day1 = time1->tm_yday;
	int year_day2 = time2->tm_yday;

	if (year_day2 < year_day1)
	{
		year_day2 += 365; // check leap year
	}

	int days_apart = year_day2 - year_day1;

	week_day1 += days_apart;
	if (week_day1 >= 7)
	{
		return 0;
	}

	return 1;
}

/**
 * Converts seconds to minutes, rounding down.
 * 
 * @param seconds The seconds.
 * @return The minutes.
 */
unsigned long seconds_to_minutes(unsigned long seconds){
	return seconds / 60;
}

/**
 * Converts minutes to hours, rounding down.
 * 
 * @param minutes The minutes.
 * @return The hours.
 */
unsigned long minutes_to_hours(unsigned long minutes){
	return minutes / 60;
}