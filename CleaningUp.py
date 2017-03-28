T = int(input())
for _ in range(T):
	n,m=map(int,input().split())
	jobsDone = set(map(int,input().split()))
	jobs = sorted(list(set(range(1,n+1)) - jobsDone))
	jobs = list(map(str,jobs))
	print(' '.join(jobs[::2]))
	print(' '.join(jobs[1::2]))



#line 5 why was the need to sort here
#adding sort solved the issue which was giving wrong answer

'''
3
6 3
2 4 1
3 2
3 2
8 2
3 8
'''