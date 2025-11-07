#include <stdio.h>
int main() {
    int a[5];
    for (int i = 0; i < 5; i++)
        scanf("%d",&a[i]);
    for (int i = 0; i < 5; i++)
        for (int j = i+1; j < 5; j++)
            if(a[j]<a[i]){
                int tmp=a[i];
                a[i]=a[j];
                a[j]=tmp;
            }
    for (int i = 0; i < 5; i++)
        printf("%d ",a[i]);
    return 0;
}