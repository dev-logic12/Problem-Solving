def solution(num_list, n)
  num_list.each_with_index.select { |_, i| i % n == 0 }.map(&:first)
end
