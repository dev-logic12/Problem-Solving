#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int solution(const char* my_string, const char* is_prefix) {
    size_t len = strlen(is_prefix);
    if (strncmp(my_string, is_prefix, len) == 0) return 1;
    return 0;
}
