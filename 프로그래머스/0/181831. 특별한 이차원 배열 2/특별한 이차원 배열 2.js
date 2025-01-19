function solution(arr) {
    const a = arr.length;

    for(let i=0; i < a; i++) {
        for(let j=i+1; j < a; j++) {
            if(arr[i][j] !== arr[j][i]) return 0;
        }
    }

    return 1;
}