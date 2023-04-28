def solution(a, b, c):
    answer = 0
    if a != b and b!=c and a!=c:
        return a+b+c 
    elif a ==b and a !=c:
        return (a + b + c)*(a*a + b*b + c*c )
    elif a ==c and a !=b:
        return (a + b + c)*(a*a + b*b + c*c )
    elif c ==b and a !=b:
        return (a + b + c)*(a*a + b*b + c*c )
    elif a == b == c:
        return  (a + b + c)*(a*a + b*b + c*c)*(a**3 + b**3 + c**3)
