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