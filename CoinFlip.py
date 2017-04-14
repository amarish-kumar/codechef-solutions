
T = int(input())
for _ in range(T):
	G = int(input())
	for X in range(G):
		headOrTail,numberOfRounds,resultAsHeadOrTail = map(int,input().split())

		result = numberOfRounds // 2
		if numberOfRounds % 2 == 1 and resultAsHeadOrTail != headOrTail:
			
			print(result+1)
		else:
			print(result)
