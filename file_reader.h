#ifndef FILE_READER_H
#define FILE_READER_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void write_str(char* filename, char* data);
char* read_str(char* filename);
void copy_file(char* filename1, char* filename2);
char* create_file_path(char* folder, char* filename);

#endif