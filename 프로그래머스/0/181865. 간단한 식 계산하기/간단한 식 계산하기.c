#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int solution(const char* binomial) {
    int a, b;
    char op;
    
    sscanf(binomial, "%d %c %d", &a, &op, &b);
    
    switch (op) {
        case '+':
            return a + b;
        case '-':
            return a - b;
        case '*':
            return a * b;
        default:
            return 0;
    }
}