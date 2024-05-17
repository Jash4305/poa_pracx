#include <stdlib.h>
#include <stdio.h>
#define BITNUM 4

int addition(int num1[], int num2[], int result[]) {
    int sum, carry = 0;
    for (int i = BITNUM - 1; i >= 0; i--)
    {
        sum = num1[i] + num2[i] + carry;
        result[i] = sum % 2; // agr sum = 2 then "0", sum = 3 then "1" or sum = 1 then "1"
        carry = sum / 2;
    }
    return carry;
}

void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
}

void shiftRight(int *c, int a[], int q[]) {
    int temp = a[0];
    
    for(int i = BITNUM - 1; i > 0; i--)
        q[i] = q[i - 1];

    q[0] = a[BITNUM - 1];
    
    for(int i = BITNUM - 1; i > 0; i--)
        a[i] = a[i-1];
        
    a[0] = *c;
    *c = 0;
}

void boothMultiplication(int m[], int q[]) {
    int a[BITNUM] = {0};
    int carry = 0; 

    printf("C\t   A\t\t   Q\t\tcount\n");
    printf("%d\t", carry);
    printArray(a, BITNUM);
    printf("\t");
    printArray(q,BITNUM);
    printf("\tInitial Value\n");

    for(int i = 0; i < BITNUM; i++) {
    
        if(q[BITNUM-1] == 1) {

            carry = addition(m, a, a); 
            shiftRight(&carry, a, q);
        }
        else 
            shiftRight(&carry, a, q);
        
        printf("%d\t", carry);
        printArray(a, BITNUM);
        printf("\t");
        printArray(q,BITNUM);
        printf("\t%d\t\n", i+1);
    }
    printf("\nProduct (in binary) : ");
    printf("%d ",carry);
    printArray(a, BITNUM);
    printArray(q, BITNUM);
}

int main() {
    
    int m[] = {0, 1, 1, 1}; // 13
    int q[] = {1, 0, 1, 1}; // 11
    

    boothMultiplication(m, q);

    return 0;  
}