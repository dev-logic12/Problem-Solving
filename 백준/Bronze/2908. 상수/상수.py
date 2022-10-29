num0, num1 = input().split()
num0 = int(num0[::-1])
num1 = int(num1[::-1])

print(num0) if num0>num1 else print(num1)