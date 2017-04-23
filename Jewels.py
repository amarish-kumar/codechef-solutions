T = int(input())

for _ in range(T):
	ori = input()
	ori = list(ori)

	unknown = input()
	unknown = list(unknown)

	result = [u for u in unknown if u in ori]
	print(len(result))