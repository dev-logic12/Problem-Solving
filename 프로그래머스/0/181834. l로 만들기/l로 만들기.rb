def solution(myString)
  myString.chars.map { |ch| ch < 'l' ? 'l' : ch }.join
end
