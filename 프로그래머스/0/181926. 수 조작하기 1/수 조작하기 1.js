function solution(n, control) {
  const move = [1, -1, 10, -10];
  const directions = ['w', 's', 'd', 'a'];

  return n + [...control].reduce((acc, c) => {
    return acc + move[directions.indexOf(c)];
  }, 0);
}
