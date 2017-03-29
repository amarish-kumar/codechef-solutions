

import math

T = int(input())
for _ in range(T):
	N = int(input())
	Skills = sorted(list(map(int,input().split())))
	minSKillDifference = 1000000000
	index = len(Skills) - 1
	while index > 0:
		temp = int(math.fabs(Skills[index]-Skills[index-1]))
		if(minSKillDifference > temp):
			minSKillDifference = temp
		index-=1
	print(minSKillDifference)