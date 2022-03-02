data = open("input.txt", "r").read().split("\n")


goal = []
busses = []
for i, bus in enumerate(data[1].split(',')):
	if bus == 'x':
		continue
	goal.append(i)
	busses.append(int(bus))

busses_init = busses.copy()

step = max(busses)
j = step - goal[busses.index(step)]
for i in range(len(busses)):
	busses[i] -= j


while True:
	print(j)
	for i in range(len(busses)):
		busses[i] -= step
		if busses[i] < goal[i]:
			busses[i] += busses_init[i]
			while busses[i] < goal[i]:
				busses[i] += busses_init[i]


	if busses == goal:
		print(j+step)
		exit()
	j += step

exit()

# step = 1
# number = 1
# print(busses)

# for i in range(len(busses)):
# 	while True:
# 		print(number, busses)
# 		if number % busses[i] == 0:
# 			step = number
# 			break
# 		number += step
# print(number)