#include <stdio.h>
#include <string.h>
int main()
{
    char st[10000];
    int i;
    scanf("%s",st);
    int len = strlen(st);
    for (i = 0; i < len; i++)
        if(st[i]!=st[len-i-1]){
            printf("The string is not Palindrome\n");
            break;
        }
    if(i==len-1)
        printf("The string is Palindrome\n");
    return 0;
}