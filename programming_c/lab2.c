#include<stdio.h>
int main(){
    int height,width;
    printf("Enter height and weight of rectangle \n");
    scanf("%d %d",&height,&width);
    float result=height*width;
    printf("Area of the rectangle is : %f",result);
    return 0;
}