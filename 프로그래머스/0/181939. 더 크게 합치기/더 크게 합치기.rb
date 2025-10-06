def solution(a, b)
  [a, b].permutation.map { |x, y| (x.to_s + y.to_s).to_i }.max
end
