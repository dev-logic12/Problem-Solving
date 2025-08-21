function solution(n, k) {
    const len = Math.floor(n / k);
    const answer = new Array(len);
    for (let i = 0; i < len; i++) {
        answer[i] = (i + 1) * k;
    }
    return answer;
}
