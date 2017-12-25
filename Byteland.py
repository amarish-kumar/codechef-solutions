
dynamicProg = {}

def calculate(goldCoin):
	if goldCoin == 0:
		return 0
	elif goldCoin in dynamicProg:
		return dynamicProg[goldCoin]
	else:
		dynamicProg[goldCoin] = max(calculate(goldCoin//2) + calculate(goldCoin//3) + calculate(goldCoin//4),goldCoin)
		return dynamicProg[goldCoin]

try:
    while True:
        print(calculate(int(input())))
        
except EOFError:
    pass 
