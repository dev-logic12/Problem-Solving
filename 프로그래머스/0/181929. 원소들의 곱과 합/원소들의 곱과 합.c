#include <stdio.h>
int solution(int num_list[], size_t num_list_len) {
    int mult = 1;
    int sum = 0;

    for(int i = 0; i < num_list_len; i++)
    {
        mult *= num_list[i];
        sum += num_list[i];
    }

    return mult < sum * sum;
}