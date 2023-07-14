def solution(ineq, eq, n, m):
    return 1 if (ineq == '<' and eq == '=' and n <= m) else \
           1 if (ineq == '>' and eq == '=' and n >= m) else \
           1 if (ineq == '>' and eq == '!' and n > m) else \
           1 if (ineq == '<' and eq == '!' and n < m) else \
           0
