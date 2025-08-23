#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int solution(const char* my_string, const char* is_prefix) {
    size_t prefix_len = strlen(is_prefix);
    size_t str_len = strlen(my_string);

    if (prefix_len > str_len) return 0;

    return strncmp(my_string, is_prefix, prefix_len) == 0 ? 1 : 0;
}
