import sys

f = open("input.txt", "r")
data = f.read().split('\n')

MAGIC_MULTIPLICATOR = 5
Y = len(data)
X = len(data[0])
dimensions_y = Y * MAGIC_MULTIPLICATOR
dimensions_x = X * MAGIC_MULTIPLICATOR


vertex = []
opened = []
closed = {}
values = []

def xy2index(x, y):
	return x * dimensions_y + y

def index2xy(i):
	x = i // (dimensions_x)
	y = i % dimensions_y
	return (x, y)

def get_h(i):
	x, y = index2xy(i)
	return (dimensions_y - y - 1) + (dimensions_x - x - 1)


for i in range(dimensions_x):
	for j in range(dimensions_y):
		index = xy2index(i, j)
					#distance, prev_vertex, h
		vertex.append([sys.maxsize,  None, get_h(index)])

		sector_x = i // X 
		sector_y = j // Y

		value = int(data[i % X][j % Y]) + sector_x + sector_y
		while value > 9:
			value -= 9

		values.append(value)

vertex[0] = [0, None, get_h(0)]
opened.append(0)


def get_f(i):
	return vertex[i][0] + vertex[i][2]

def get_next():
	candidate_id = None
	candidate_f = None

	opened.sort(key=get_f)
	return opened[0]

def get_adjusted(i):
	arr = []

	col = i % dimensions_y
	row = i // dimensions_x

	if col + 1 < dimensions_y:
		arr.append(xy2index(row, col+1))
	if col - 1 >= 0:
		arr.append(xy2index(row, col-1))
	if row + 1 < dimensions_x:
		arr.append(xy2index(row+1, col))
	if row - 1 >= 0:
		arr.append(xy2index(row-1, col))

	return arr	

best = 999999

while True:
	current_v = get_next()

	for next_v in get_adjusted(current_v):

		if vertex[next_v][0] > vertex[current_v][0] + values[next_v]:
			vertex[next_v][0] = vertex[current_v][0] + values[next_v]
			vertex[next_v][1] = current_v

			if vertex[next_v][2] == 0:
				print(vertex[next_v][0])
				exit()

		if next_v not in opened and next_v not in closed:
			opened.append(next_v)

	opened.remove(current_v)
	closed[current_v] = 1
