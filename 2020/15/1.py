data = open("input.txt", "r").read().split(",")


memory = {}
last_number = 0
for j, num in enumerate(data):
	last_number = num
	memory[int(num)] = [j]


def get_next(last_number, i):
	global memory

	if last_number in memory and len(memory[last_number]) >= 2:
		# print('a',memory[last_number][-1], memory[last_number][-2], memory)
		new_number = memory[last_number][-1] - memory[last_number][-2]
		if new_number in memory:
			memory[new_number].append(i)
		else:
			memory[new_number] = [i]
		return new_number
	else:
		if 0 in memory:
			memory[0].append(i)
		else:
			memory[0] = [i]
		return 0


for i in range(j+1, 2020):
	last_number = get_next(last_number, i)
print(last_number)
assert last_number == 852