function solution(arr) {
    const n = Math.max(arr.length, ...arr.map(row => row.length)); 
    return arr.map(row => [...row, ...Array(n - row.length).fill(0)]) 
              .concat(Array(n - arr.length).fill().map(() => Array(n).fill(0)));
}
