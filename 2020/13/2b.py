data = open("test_input.txt", "r").read().split("\n")


busses = []
busses_init = []
goals = []
for i, bus in enumerate(data[1].split(',')):
	if bus == 'x':
		continue
	goals.append(i)
	busses.append(int(bus))
	busses_init.append(int(bus))


step = 1
number = 1
print(busses)
print(goals)
for i in range(len(busses)):
	while True:
		print(number, step)
		# print('qqqq', number % busses_init[i], (busses_init[i] - goals[i]) % busses_init[i])
		if (number % busses_init[i]) == (busses_init[i] - goals[i]) % busses_init[i]:
			# print('qqqq', number, busses_init[i], goals[i])
			prev_value = busses_init[i-1] if i-1 >= 0 else 1
			# print('asdf', prev_value, busses_init[i])
			step = prev_value * busses_init[i]
			# number += step
			break
		number += step

		# if number > 20:
		# 	break

print(number)