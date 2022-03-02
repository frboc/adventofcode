data = open("input.txt", "r").read().split("\n")

goal, busses = data
goal = int(goal)
busses = [int(a) for a in busses.split(',') if a != 'x']


waiting_time = 0
while True:
	for bus in busses:
		if (goal + waiting_time) % bus == 0:
			result = bus * waiting_time
			print(result)
			assert result == 370
			exit()
	waiting_time += 1