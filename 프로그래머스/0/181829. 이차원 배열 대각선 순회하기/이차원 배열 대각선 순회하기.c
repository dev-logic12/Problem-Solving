#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int** board, size_t board_rows, size_t board_cols, int k) {
    int answer = 0;
    for(int r = 0; r < board_rows; r++) {
        for(int c = 0; c < board_cols; c++) {
            if(r + c > k) break;
            answer += board[r][c];
        }
    }
    return answer;
}