data = list(map(lambda x:x.split(), open("input.txt", "r").read().split("\n")))


pointer = 0
acc = 0
visited = {}
while True:
	if pointer in visited:
		break
	visited[pointer] = None

	operation, argument = data[pointer]
	argument = int(argument)
	if operation == 'acc':
		acc += argument
	if operation == 'jmp':
		pointer += argument
		continue
	pointer += 1

print(acc)
assert acc == 1446