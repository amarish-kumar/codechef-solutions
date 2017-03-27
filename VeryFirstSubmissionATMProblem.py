cashToWithDraw,cashInAccount = map(float,input().split())
balance = float(cashInAccount)-float(0.50)

if(cashToWithDraw%5 == 0 and cashToWithDraw <= balance):
	balance = balance - cashToWithDraw
else:
	balance = cashInAccount

print(format(balance,'.2f'))
