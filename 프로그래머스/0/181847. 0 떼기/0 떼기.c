#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

char* solution(const char* n_str) {
    char* answer = n_str - 1;
    while(*++answer) {
        if(*answer != '0') break;
    }
    return answer;
}