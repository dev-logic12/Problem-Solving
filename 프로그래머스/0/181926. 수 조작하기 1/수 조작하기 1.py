def solution(n, control):
    move = [1, -1, 10, -10]
    directions = ['w', 's', 'd', 'a']
    
    return n + sum(move[directions.index(c)] for c in control)
