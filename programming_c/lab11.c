#include<stdio.h>
// function declarations
int add(int n1, int n2); // function for addition
int sub(int n1, int n2); // function for subtraction
int mul(int n1, int n2); // function for multiplication
float div(int n1, int n2); // function for division

int main() {
    int num1 = 10; // first number
    int num2 = 5;  // second number
    printf("Addition: %d\n", add(num1,num2)); // calling add function
    printf("Subtraction: %d\n", sub(num1,num2)); // calling sub function
    printf("Multiplication: %d\n", mul(num1,num2)); // calling mul function
    printf("Division: %.2f\n", div(num1,num2)); // calling div function
    return 0;
}

// function definitions

// function for addition
int add(int n1, int n2) {
    return (n1 + n2);
}

// function for subtraction
int sub(int n1, int n2) {
    return (n1 - n2);
}

// function for multiplication
int mul(int n1, int n2) {
    return (n1 * n2);
}

// function for division
float div(int n1, int n2) {
    return ((float)n1 / (float)n2);
}