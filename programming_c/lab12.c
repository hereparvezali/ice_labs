#include <stdio.h>
struct student {
    char name[50];
    int roll;
    float mark;
};

int main() {
    struct student s[5]; //array of structures
    int i;
    printf("Enter information of students:\n");
    for(i = 0; i < 5; ++i) {
        s[i].roll = i + 1;
        printf("\nFor roll number %d,\n", s[i].roll);
        printf("Enter name: ");
        scanf("%s", s[i].name);
        printf("Enter mark: ");
        scanf("%f", &s[i].mark);
    }
    printf("\nDisplaying Information:\n");
    for(i = 0; i < 5; ++i) {
        printf("\nRoll number: %d\n", i + 1);
        printf("Name: ");
        puts(s[i].name);
        printf("Mark: %.1f", s[i].mark);
        printf("\n");
    }
    return 0;
}