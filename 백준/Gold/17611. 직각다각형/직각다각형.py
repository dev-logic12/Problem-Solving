hn = [0]*1001000
wn = [0]*1001000

height = []
width = []
for n in range(int(input())):
    x, y = map(int, input().split())
    y = y + 500000
    x = x + 500000

    width.append(x)
    height.append(y)

maxW = max(width)
minW = min(width)

maxH = max(height)
minH = min(height)

a1, b1 = width[0],width[-2]
a2, b2 = height[0],height[-2]

wn[min(a1,b1)] += 1
wn[max(a1,b1)] -= 1

hn[min(a2,b2)] += 1
hn[max(a2,b2)] -= 1

for i in range(n-1):

    a = min(height[i], height[i+1])
    b = max(height[i], height[i+1])
    if a != b:
        hn[a] += 1
        hn[b] -= 1

    c = min(width[i], width[i+1])
    d = max(width[i], width[i+1])
    if c != d:
        wn[c] += 1
        wn[d] -= 1
    
prefix_h = [0]*1001000
prefix_w = [0]*1001000

for h in range(minH-2, maxH):
    prefix_h[h+1] = prefix_h[h] + hn[h+1]

for k in range(minW-2, maxW):
    prefix_w[k+1] = prefix_w[k] + wn[k+1]

print(max(max(prefix_h),max(prefix_w)))