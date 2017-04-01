T = int(input())


for _ in range(T):
	N = int(input())
	Songs = list(map(int,input().split()))
	pos = int(input())
	UncleJohny = Songs[pos-1]
	Songs = sorted(Songs)
	pos = Songs.index(UncleJohny)
	print(pos+1)


'''
3
4
1 3 4 2
2
5
1 2 3 9 4s
5
5
1 2 3 9 4 
1
'''


'''
3
4
1

'''