#include "file_reader.h"

/**
 * Write data to a file.
 * 
 * @param filename The file to write to.
 * @param data The data to write.
 */
void write_str(char* filename, char* data){
	FILE *fp = fopen(filename, "w+");
	fputs(data, fp);
	fclose(fp);
}

/**
 * Read data from a file.
 * 
 * @param filename The file to read from.
 * @return The data.
 */
char* read_str(char* filename){
	char* buffer = NULL;
	FILE* fp = fopen(filename, "r+");
	if(fp){
		fseek(fp, 0, SEEK_END);
		int length = ftell(fp);
		fseek(fp, 0, SEEK_SET);
		buffer = malloc(length);
		if (buffer)
		{
			fread(buffer, 1, length, fp);
		}
	  	fclose(fp);
  	}
	return buffer;
}