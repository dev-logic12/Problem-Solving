function solution(arr) {
    answer = arr.every((r, i) => r.every((_, j) => arr[i][j] === arr[j][i])) ? 1 : 0;
    return answer
}