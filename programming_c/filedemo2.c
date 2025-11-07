#include <stdio.h>
#include <string.h>
int main(){
	FILE *file;
	char name[200]= "parvez ali is the best boy";
	int len = strlen(name);
	file = fopen("test.txt","w");
	if(file==NULL)
		printf("does not exist\n");
	else{
		printf("file is opened\n");
		fputc(' ',file);
		for (int i = 0; i < len; i++)
		{
			fputc(name[i],file);
		}
		fclose(file);
	}
	 
}