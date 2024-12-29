#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* rny_string) {
    int len = strlen(rny_string);
    char* answer = (char*)malloc(sizeof(char) * 200);
    int j = 0;
    for(int i = 0; i < len ; i++)
    {
        if(rny_string[i] == 'm')
        {
            answer[j] = 'r';
            j++;
            answer[j] = 'n';
        }
        else
            answer[j] = rny_string[i];
        j++;
    }
    answer[j] = '\0';
    return answer;
}