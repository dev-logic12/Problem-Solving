#include <stdio.h>
#include <string.h> 
#include <stddef.h> 

int solution(const char* order[], size_t order_len) {
    int total_price = 0;

    for (size_t i = 0; i < order_len; i++) {
        if (strstr(order[i], "cafelatte") != NULL) {
            total_price += 5000; // 카페라떼 가격
        } else {
            total_price += 4500; // 다른 음료 가격
        }
    }

    return total_price;
}
