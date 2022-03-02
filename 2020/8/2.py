from copy import deepcopy

data = list(map(lambda x:x.split(), open("input.txt", "r").read().split("\n")))


def do_magic(data):
	pointer = 0
	acc = 0
	visited = {}
	while True:
		if pointer in visited:
			return False
		visited[pointer] = None

		operation, argument = data[pointer]
		argument = int(argument)
		if operation == 'acc':
			acc += argument
		if operation == 'jmp':
			pointer += argument - 1
		pointer += 1
		if pointer >= len(data):
			return acc

for i in range(len(data)):
	if data[i][0] == 'jmp':
		new_data = deepcopy(data)
		new_data[i][0] = 'nop'
		result = do_magic(new_data)
		if result:
			print(result)
			assert result == 1403
			exit()
		continue

	if data[i][0] == 'nop':
		new_data = deepcopy(data)
		new_data[i][0] = 'jmp'
		result = do_magic(new_data)
		if result:
			print(result)
			assert result == 1403
			exit()
