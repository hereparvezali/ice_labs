#include <stdio.h>
int main()
{
    int number;
    printf("Enter a number\n");
    scanf("%d", &number);
    if (number % 2 == 0)
    {
        printf("The number is EVEN\n");
    }
    else
        printf("The number is ODD\n");
    return 0;
}