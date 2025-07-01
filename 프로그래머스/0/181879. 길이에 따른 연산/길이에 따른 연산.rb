def solution(num_list)
  if num_list.length >= 11
    num_list.sum
  else
    num_list.inject(1) { |product, n| product * n }
  end
end
