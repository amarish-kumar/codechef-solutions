import sys
T = int(input())


for _ in range(T):
	number_of_cars = int(input())
	car_speeds = list(map(int, sys.stdin.readline().split()))

	if number_of_cars == 1:
		print(1)
	else:
		output = 1

		for car_speed in range(1,number_of_cars):
			
			if car_speeds[car_speed] > car_speeds[car_speed-1]:
				car_speeds[car_speed] = car_speeds[car_speed-1]

			else:
				output+=1

		print(output)



'''
the problem focused on fast IO 
sys.stdin.readline().split() is faster than 
input().split()

python access local variables much faster than global vars

'''
