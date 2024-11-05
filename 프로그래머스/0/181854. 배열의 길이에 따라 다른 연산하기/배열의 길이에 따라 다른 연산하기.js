const solution = (arr, n) => arr.map((v, i) => v + (arr.length-i) % 2 * n);
