function solution(board, k) {
  let sum = 0;
  const rows = board.length;
  const cols = board[0].length;
  
  for (let x = 0; x < rows; x++) {
    for (let y = 0; y < cols; y++) {
      if (x + y <= k) {
        sum += board[x][y];
      }
    }
  }
  
  return sum;
}
