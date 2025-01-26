#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

char* solution(const char* myString) {
    char* answer = (char*)malloc(sizeof(char)*(strlen(myString)+1));
    memcpy(answer, myString, strlen(myString)+1);
    for(int i=0;i<strlen(answer);i++){
        if(answer[i]=='a'||answer[i]=='A'){answer[i]='A';}
        else{answer[i]=tolower(answer[i]);}
    }
    return answer;
}