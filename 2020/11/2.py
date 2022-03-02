from copy import deepcopy

state = list(map(list, open("input.txt", "r").read().split("\n")))

X = len(state)
Y = len(state[0])

def plot(state):
	for i in range(X):
		for j in range(Y):
			print(state[i][j], end='')

		print()

def how_many_occupied_see(i, j, state):
	counter = 0
	directions = []
	for a in (-1, 0, 1):
		for b in (-1, 0, 1):
			if a == 0 and b == 0:
				continue
			I = i+a
			J = j+b
			if I < 0 or J < 0 or I >= X or J >= Y:
				continue
			directions.append((a, b))

	while directions:
		x, y = directions.pop()
		z = 1
		while True:
			a = i + x * z
			b = j + y * z
			if a < 0 or b < 0 or a >= X or b >= Y:
				break
			if state[a][b] == '#':
				counter += 1
				break
			if state[a][b] == 'L':
				break
			z += 1


	return counter


while True:
	old_state = state
	state = deepcopy(state)


	for i in range(X):
		for j in range(Y):
			if old_state[i][j] == 'L':
				if how_many_occupied_see(i, j, old_state) == 0:
					state[i][j] = '#'

			elif old_state[i][j] == '#':
				if how_many_occupied_see(i, j, old_state) >= 5:
					state[i][j] = 'L'


	if old_state == state:
		break

counter = 0
for row in state:
	for char in row:
		if char == '#':
			counter += 1

# plot(state)
print(counter)
assert counter == 2180