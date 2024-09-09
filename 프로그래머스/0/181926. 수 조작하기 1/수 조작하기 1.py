def solution(n, control):
    moves = [1, -1, 10, -10]
    directions = ['w', 's', 'd', 'a']
    
    return n + sum(moves[directions.index(c)] for c in control)
