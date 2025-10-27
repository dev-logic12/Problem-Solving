function solution(a, b) {
  return Math.max(a * 10 ** String(b).length + b, b * 10 ** String(a).length + a);
}
