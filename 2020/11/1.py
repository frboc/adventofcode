from copy import deepcopy

state = list(map(list, open("input.txt", "r").read().split("\n")))

X = len(state)
Y = len(state[0])

def plot(state):
	for i in range(X):
		for j in range(Y):
			print(state[i][j], end='')

		print()


def get_adjusted(i, j, state):
	res = []
	for a in (-1, 0, 1):
		for b in (-1, 0, 1):
			if a == 0 and b == 0:
				continue
			I = i+a
			J = j+b
			if I < 0 or J < 0 or I >= X or J >= Y:
				continue
			res.append((I, J))
	return res


while True:
	old_state = state
	state = deepcopy(state)


	for i in range(X):
		for j in range(Y):
			if old_state[i][j] == 'L':
				can_ocupy = True
				for a, b in get_adjusted(i, j, old_state):
					if old_state[a][b] == '#':
						can_ocupy = False
				if can_ocupy:
					state[i][j] = '#'
			elif old_state[i][j] == '#':
				occupied_counter = 0
				for a, b in get_adjusted(i, j, old_state):
					if old_state[a][b] == '#':
						occupied_counter += 1
				if occupied_counter >= 4:
					state[i][j] = 'L'


	if old_state == state:
		break

counter = 0
for row in state:
	for char in row:
		if char == '#':
			counter += 1

print(counter)
assert counter == 2489
