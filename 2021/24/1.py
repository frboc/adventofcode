f = open("input.txt", "r")
data = []
for row in f.read().split("\n"):
	data.append(row.split(' '))


def magic(input):
	memory = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
	for instruction in data:
		if instruction[0] == 'inp':
			memory[instruction[1]] = int(input.pop(0))
			#print('read', memory[instruction[1]])
			continue

		if instruction[0] == 'mul':
			if instruction[2] in memory:
				#print(memory[instruction[1]], '*', memory[instruction[2]])
				memory[instruction[1]] *= memory[instruction[2]]
			else:
				memory[instruction[1]] *= int(instruction[2])
			continue

		if instruction[0] == 'add':
			if instruction[2] in memory:
				memory[instruction[1]] += memory[instruction[2]]
			else:
				memory[instruction[1]] += int(instruction[2])
			continue

		if instruction[0] == 'div':
			if instruction[2] in memory:
				#print(memory[instruction[1]], '/',  memory[instruction[2]])
				memory[instruction[1]] = int(memory[instruction[1]] / memory[instruction[2]])
			else:
				#print(memory[instruction[1]], '/', int(instruction[2]))
				memory[instruction[1]] = int(memory[instruction[1]] / int(instruction[2]))
			continue

		if instruction[0] == 'mod':
			if instruction[2] in memory:
				memory[instruction[1]] = memory[instruction[1]] % memory[instruction[2]]
			else:
				memory[instruction[1]] = memory[instruction[1]] % int(instruction[2])
			continue

		if instruction[0] == 'eql':
			if instruction[2] in memory:
				#print(memory[instruction[1]], 'eq', memory[instruction[2]])
				memory[instruction[1]] = 1 if memory[instruction[1]] == memory[instruction[2]] else 0
			else:
				#print(memory[instruction[1]], 'eq1', int(instruction[2]))
				memory[instruction[1]] = 1 if memory[instruction[1]] == int(instruction[2]) else 0
			continue

	print(memory)
	if memory['z'] == '0':
		return True
	print(memory['z'])
	return False




magic(list('91897399498995'))
exit()

for num in range(99999999999999, 11111111111111, -1):
	print(num)
	num = list(str(num))
	if '0' in num:
		continue
	if magic(num.copy()):
		print(''.join(num))
		#exit()
