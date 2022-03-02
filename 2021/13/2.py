import functools
import csv

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

def fold_hor(pos):
	a = [matrix[i][:pos] for i in range(len(matrix))]
	b = [matrix[i][pos+1:] for i in range(len(matrix))]

	bigger = a if len(a[0]) >= len(b[0]) else b
	smaller = a if len(a[0]) < len(b[0]) else b
	difference = len(bigger) - len(smaller)

	for row in bigger:
		print(row)
	print()
	for row in smaller:
		print(row)
	print()

	for x in range(len(bigger)):
		for y in range(len(bigger[0])):
			if smaller[x][y] == 1:
				bigger[x][(y+difference+1)*-1] = 1
	return bigger

for axis, value in splits:
	if axis == 'y':
		a = matrix[:value]
		b = matrix[value+1:]
		matrix = fold(a, b)
	else:
		matrix = fold_hor(value)


def is_arr_empty(a):
	for val in a:
		if val != 0:
			return False
	return True


def is_column_empty(col):
	for row in matrix:
		if row[col] != 0:
			return False
	return True


for x in range(len(matrix)):
	for y in range(len(matrix[0])):
		if matrix[x][y] == 1:
			print('*', end='')
		else:
			print('-', end='')
	print()
