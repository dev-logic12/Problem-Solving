def solution(arr)
  rows = arr.length
  cols = arr[0].length

  if rows > cols
    arr.each do |row|
      (rows - cols).times { row << 0 }
    end
  elsif cols > rows
    (cols - rows).times { arr << Array.new(cols, 0) }
  end

  arr
end
