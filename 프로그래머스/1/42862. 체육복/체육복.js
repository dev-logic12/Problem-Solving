function solution(n, lost, reserve) {
    // 여분의 체육복이 있지만 도난당한 학생들을 먼저 제거
    let actualReserve = reserve.filter(r => !lost.includes(r));
    let actualLost = lost.filter(l => !reserve.includes(l));

    // 여분의 체육복이 있는 학생들 정렬
    actualReserve.sort((a, b) => a - b);
    actualLost.sort((a, b) => a - b);

    let answer = n - actualLost.length;

    // 체육복을 빌려줄 수 있는지 확인
    actualReserve.forEach(r => {
        let index = actualLost.findIndex(l => Math.abs(l - r) === 1);
        if (index !== -1) {
            answer++;
            actualLost.splice(index, 1); // 빌려준 학생은 목록에서 제거
        }
    });

    return answer;
}
