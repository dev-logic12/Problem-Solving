#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* myString) {
    int len = strlen(myString);
    char* answer = malloc(len + 1);
    if (!answer) return NULL;
    
    for (int i = 0; i < len; i++) {
        answer[i] = myString[i] < 'l' ? 'l' : myString[i];
    }
    answer[len] = '\0';
    return answer;
}

int main() {
    char myString[] = "abcdefghijklm";
    char* result = solution(myString);
    
    if (result) {
        printf("Modified string: %s\n", result);
        free(result);
    } else {
        printf("Memory allocation failed\n");
    }

    return 0;
}