def solution(a, b)
  ab = (a.to_s + b.to_s).to_i
  ba = (b.to_s + a.to_s).to_i
  ab >= ba ? ab : ba
end
