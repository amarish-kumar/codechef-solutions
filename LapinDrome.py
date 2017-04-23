T = int(input())

for _ in range(T):
	_input = input()
	
	length=len(_input)
	midpoint = length//2

	if length % 2 == 0:
		subset = _input[midpoint:]
		_input = _input[:midpoint]
		
		
	else:
		subset = _input[midpoint + 1 :]
		_input = _input[:midpoint]
	

	print('YES') if ''.join(sorted(subset)) == ''.join(sorted(_input)) else print('NO')



