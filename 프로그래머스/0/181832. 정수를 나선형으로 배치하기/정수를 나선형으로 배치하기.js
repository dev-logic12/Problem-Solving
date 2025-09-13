function solution(n) {
  const a = Array.from({ length: n }, () => Array(n).fill(0));
  let num = 1, top = 0, bottom = n - 1, left = 0, right = n - 1;

  while (top <= bottom && left <= right) {
    for (let j = left; j <= right; j++) a[top][j] = num++;
    top++;
    for (let i = top; i <= bottom; i++) a[i][right] = num++;
    right--;
    for (let j = right; j >= left; j--) a[bottom][j] = num++;
    bottom--;
    for (let i = bottom; i >= top; i--) a[i][left] = num++;
    left++;
  }
  return a;
}
