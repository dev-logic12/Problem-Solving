def solution(picture, k):
    row_len = len(picture)
    col_len = len(picture[0])

    new_picture = []

    for row in picture:
        new_row = ''
        for pixel in row:
            new_row += pixel * k
        new_picture.extend([new_row] * k)

    return new_picture
