
def solution(keyinput, board):
    answer = []
    x = 0
    y = 0
    for i in keyinput:
        if i == 'right':
            x +=1
        elif i == 'left':
            x -=1
        elif i == 'up':
            y += 1
        elif i == 'down':
            y -= 1
        if abs(x) >= (board[0] // 2):
            x = (x // abs(x)) * (board[0] // 2)
        if abs(y) >= (board[1] // 2):
            y = (y // abs(y)) * (board[1] // 2)
    return [x, y]