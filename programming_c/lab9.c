#include <stdio.h>
int main()
{
    int num1, num2, num3;
    int *p1, *p2, *p3;
    printf("Enter three numbers: ");
    scanf("%d %d %d", &num1, &num2, &num3);
    p1 = &num1; //assigning pointers to each number
    p2 = &num2;
    p3 = &num3;
    if(*p1 > *p2 && *p1 > *p3) //comparing numbers using pointers
        printf("Largest = %d",*p1);
    else if(*p2 > *p1 && *p2 > *p3)
        printf("Largest = %d",*p2);
    else
        printf("Largest = %d",*p3);
    return 0;
}