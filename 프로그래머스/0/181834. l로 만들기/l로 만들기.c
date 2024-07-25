#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* myString) {
    int len = strlen(myString);
    char* answer = (char*)malloc(len + 1);
    for(int i = 0; i < len; i++) {
        answer[i] = myString[i] < 'l' ? 'l' : myString[i];
    }
    answer[len] = '\0';
    return answer;
}

int main() {
    char myString[] = "abcdefghijklm";
    char* result = solution(myString);
    printf("Modified string: %s\n", result);
    free(result);
    return 0;
}
