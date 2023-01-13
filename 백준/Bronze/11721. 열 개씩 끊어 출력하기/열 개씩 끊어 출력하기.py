n = input()
for i in range(0, len(n), 10):	# 인덱스 0을 시작으로 n 길이의 전 까지, 10씩
	print(n[i:i+10])