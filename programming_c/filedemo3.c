#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main(){
	FILE *file;
	char name[200];
	gets(name);
	file = fopen("test.txt","w");
	if(file==NULL)
		printf("does not exist\n");
	else{
		fputs(name,file);
		fclose(file);
	}
	
}