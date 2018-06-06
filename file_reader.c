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


void copy_file(char* filename1, char* filename2){
	char* data = read_str(filename1);
	write_str(filename2, data);
	free(data);
}

char* create_file_path(char* folder, char* filename){
	int folder_len = strlen(folder);
	int filename_len = strlen(filename);

	int path_len = folder_len + filename_len;

	char* buffer = malloc(sizeof(char) * (path_len + 1));

	strncpy(buffer, folder, folder_len);
	strcpy(buffer + folder_len, filename);

	return buffer;
}