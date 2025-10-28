def solution(num_list, n)
  result = []
  num_list.each_with_index do |num, i|
    result << num if i % n == 0
  end
  result
end
