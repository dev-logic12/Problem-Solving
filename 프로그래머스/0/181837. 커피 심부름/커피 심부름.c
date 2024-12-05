#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* order[], size_t order_len) {
    int answer = 0;
    int count =0;

    for(int i=0;i<order_len;i++)
    {
        if(strstr(order[i], "cafelatte") != NULL)
            count ++;
    }
    answer = count*5000 + (order_len-count)*4500;
    return answer;
}