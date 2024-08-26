def solution(n, control)
  control.each_char do |char|
    case char
    when 'w'
      n += 1
    when 's'
      n -= 1
    when 'd'
      n += 10
    when 'a'
      n -= 10
    end
  end
  n
end
