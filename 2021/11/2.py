
f = open("input.txt", "r")
data_raw = f.read()
data = data_raw.split("\n")

for i, row in enumerate(data):
	data[i] = list(data[i])

X = len(data)
Y = len(data[0])
STEPS = 200

def is_index_valid(i, j):
	if i>=0 and j>=0 and i<X and j<Y:
		return True
	return False

def get_adjusted(i, j):
	res = []
	for x in [i-1, i, i+1]:
		for y in [j-1, j, j+1]:
			if is_index_valid(x, y):
				res.append((x, y))
	res.remove((i, j))
	return res


def get_empty_matice():
	return [[0] * X for i in range(Y)]

def begin_step():
	res = []
	for i in range(X):
		for j in range(Y):
			value = data[i][j];
			data[i][j] = int(data[i][j]) + 1
			if data[i][j] > 9:
				res.append((i, j))
	return res

def flash(x, y):
	data[x][y] = int(data[x][y]) + 1
	adjusted = get_adjusted(x, y)
	for a,b in adjusted:
		data[a][b] = int(data[a][b]) + 1
		if (data[a][b] == 10):
			flash(a, b)



counter = 0
step = 0
while True:
	flashing = begin_step()
	for f in flashing:
		flash(f[0], f[1])

	inner_counter = 0
	for i in range(X):
		for j in range(Y):
			if (data[i][j] > 9):
				counter += 1
				inner_counter += 1
				data[i][j] = 0
	print(inner_counter)
	if inner_counter == X * Y:
		exit()
	step += 1
