#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int numbers[], size_t numbers_len, int n) {
    int answer = 0;
    for(int i = 0;i<numbers_len;i++){
        answer+=numbers[i];
        if(answer>n){
            break;
        }
    }
    return answer;
}