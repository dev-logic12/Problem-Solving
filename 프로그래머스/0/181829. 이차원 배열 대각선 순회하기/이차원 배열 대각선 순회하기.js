function solution(board, k) {
  let sum1 = 0;
  for (let x = 0; x < board.length; x++) {
    for (let y = 0; y < board[0].length; y++) {
      if (x + y <= k) sum1 += board[x][y];
    }
  }
  return sum1;
}