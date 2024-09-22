#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int arr[], size_t arr_len, int k) {
    for(int i = 0; i < arr_len; i++) {
        if(k & 1) arr[i] *= k;
        else arr[i] += k;
    }
    return arr;
}