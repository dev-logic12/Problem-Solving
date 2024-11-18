#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* myString) {
    int len = strlen(myString);
    char* answer = (char*)malloc(len + 1);
    strcpy(answer, myString);
    char* ptr = answer - 1;
    while(*++ptr) {
        if(*ptr >= 'A' && *ptr <= 'Z') *ptr += 'a' - 'A';
        if(*ptr == 'a') *ptr = 'A';
    }
    return answer;
}