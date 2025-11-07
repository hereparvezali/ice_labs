#include <stdio.h>
int main()
{
    FILE *fptr; // file pointer
    char name[20]; // name variable
    int roll; // roll variable
    fptr = fopen("test.txt", "w"); // opening file in write mode
    if(fptr == NULL) // checking if file is opened successfully
    {
        printf("Error!");
        return 1;
    }
    printf("Enter your name: "); // taking user input for name
    scanf("%s", name);
    printf("Enter your roll: "); // taking user input for roll
    scanf("%d", &roll);
    fprintf(fptr, "Name: %s\nRoll: %d\n", name, roll); // writing data to file
    fclose(fptr); // closing file
    printf("File created successfully\n");
    return 0;
}