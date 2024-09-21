def solution(board, k)
  sum = 0
  
  board.each_with_index do |row, i|
    row.each_with_index do |value, j|
      if i + j <= k
        sum += value
      end
    end
  end
  
  return sum
end
