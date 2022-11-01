a = int(input())

line = 0 
b = 0
while a > b :
    line += 1
    b += line 
gap = b - a 
if line % 2 == 0:
    top = line - gap
    under = gap + 1 
else:
    top = gap + 1
    under = line - gap
print(f'{top}/{under}')