#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(const char* my_string, const char* is_prefix) {
    int answer = 0;
    if(strstr(my_string,is_prefix)==my_string) answer=1;
    return answer;
}