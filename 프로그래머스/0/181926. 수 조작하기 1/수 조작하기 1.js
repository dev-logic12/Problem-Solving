function solution(n, control) {
  const move = { w: 1, s: -1, d: 10, a: -10 };
  let total = 0;

  for (const c of control) {
    total += move[c];
  }

  return n + total;
}
