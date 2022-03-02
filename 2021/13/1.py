f = open("input.txt", "r")
raw_data = f.read()

points = []
splits = []
is_point = True
dimension_x, dimension_y = 0, 0

for row in raw_data.split("\n"):
	if row == '':
		is_point = False
	elif is_point:
		x, y = row.split(',')
		dimension_x = max(dimension_x, int(x))
		dimension_y = max(dimension_y, int(y))
		points.append((int(y), int(x)))
	else:
		text, num = row.split('=')
		splits.append((text[-1], int(num)))

dimension_x += 1
dimension_y += 1

matrix = [[0] * dimension_x for i in range(dimension_y)]

for x, y in points:
	matrix[x][y] = 1

def is_valid_index(arr, i):
	return i >= 0 and i < len(arr)

def transform(a):
	dim = max(len(a), len(a[0]))
	new = [[0] * dim for i in range(dim)]

	for x in range(dim):
		for y in range(dim):
			try:
				new[y][x] = a[x][y]
			except IndexError:
				pass
	return new

def flip(a):
	new = []
	for i in range(max(len(a),len(a[0]))):
		new.append(a[-i-1])
	return new


def fold(a, b):
	b.reverse()
	bigger = a if len(a) >= len(b) else b
	smaller = a if len(a) < len(b) else b
	difference = len(bigger) - len(smaller)

	for x in range(len(bigger)):
		for y in range(len(bigger[0])):
			try:
				if smaller[x][y] == 1:
					bigger[x+difference][y] = 1
			except IndexError:
				pass
	return bigger

for axis, value in splits:
	if axis == 'x':
		matrix = transform(matrix)
	a = matrix[:value]
	b = matrix[value+1:]

	matrix = fold(a, b)

	if axis == 'x':
		matrix = transform(matrix)
	break


counter = 0
for row in matrix:
	for val in row:
		if val == 1:
			counter += 1

print(counter)

