#include <stdio.h>
int main()
{
    FILE *fptr; // file pointer
    char name[20]; // name variable
    int roll; // roll variable
    fptr = fopen("test.txt", "r"); // opening file in read mode
    if(fptr == NULL) // checking if file is opened successfully
    {
        printf("Error!");
        return 1;
    }
    fscanf(fptr, "Name: %s\nRoll: %d\n", name, &roll); // reading data from file
    printf("Name: %s\nRoll: %d\n", name, roll); // printing data to console
    fclose(fptr); // closing file
    return 0;
}