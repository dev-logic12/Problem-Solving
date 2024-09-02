def solution(picture, k)
  re_picture = []

  picture.each do |row|
    re_row = row.chars.map { |char| char * k }.join
    
    k.times { re_picture << re_row }
  end

  re_picture
end
