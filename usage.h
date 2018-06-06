#ifndef USAGE_H
#define USAGE_H

#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <unistd.h>
#include <string.h>
#include "file_reader.h"
#include "time_utils.h"

int m_sleep(double seconds);
void daemon_mode(int argc, char* argv[]);
void print_usage(int argc, char* argv[]);
void help(void);

#endif