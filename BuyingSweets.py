T = int(input())

for _ in range(T):
	N,k = map(int,input().split())
	notes = list(map(int,input().split()))
	total_amount = sum(notes)
	temp =  total_amount % k

	if temp == 0:
		print(total_amount//k)
		continue

	else:
		_min = min(notes)
		if _min <= temp:
			print(-1)
			continue
		print(total_amount//k)