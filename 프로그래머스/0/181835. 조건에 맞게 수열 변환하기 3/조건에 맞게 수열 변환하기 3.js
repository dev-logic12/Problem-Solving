function solution(arr, k) {
    return k%2 === 0 ? arr.map(i=> k+i) : arr.map(i=> k*i)
}