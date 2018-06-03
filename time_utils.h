#ifndef TIME_DEF_H
#define TIME_DEF_H

#include <time.h>

struct tm * get_time(void);
int on_same_date(struct tm * time1, struct tm * time2);
unsigned long seconds_to_minutes(unsigned long seconds);
unsigned long minutes_to_hours(unsigned long minutes);

#endif