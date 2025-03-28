#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* mstr) {
    int len = strlen(mstr);
    char* str = (char*)calloc(0, sizeof(char) * len);

    for(unsigned short i = 0; i < len; i ++)
        str[i] = (mstr[i] | 0x20) - 0x20;

    return str;
}