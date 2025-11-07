#include <stdio.h>
int main(){
	FILE *file;
	file = fopen("test.txt","w");
	if(file==NULL)
		printf("does not exist\n");
	else{
		printf("file is opened\n");
		fclose(file);
	}
	 
}