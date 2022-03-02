import copy

f = open("input.txt", "r")
raw_data = f.read().split("\n")

state = []
for row in raw_data:
	state.append(list(row))


def plot(state):
	for row in state:
		print(''.join(row))
	print()

X = len(state)
Y = len(state[0])

plot(state)

step = 0
while True:
	step += 1
	move = False
	old_state = copy.deepcopy(state)
	for i in range(X):
		for j in range(Y):
			j1 = (j+1) % Y
			if old_state[i][j] == '>' and old_state[i][j1] == '.':
				move = True
				state[i][j1] = '>'
				state[i][j] = '.'

	old_state = copy.deepcopy(state)
	for i in range(X):
		for j in range(Y):
			i1 = (i+1) % X
			if old_state[i][j] == 'v' and old_state[i1][j] == '.':
				move = True
				state[i1][j] = 'v'
				state[i][j] = '.'
	if not move:
		break

print(step)