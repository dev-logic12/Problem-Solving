def solution(numbers, n)
  sum = 0
  numbers.each do |num|
    sum += num
    return sum if sum > n
  end
end
