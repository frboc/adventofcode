import sys

f = open("input.txt", "r")
data = f.read().split('\n')

Y = len(data) 
X = len(data[0])

vertex = []
unvisited = []
visited = []
values = []

def xy2index(x, y):
	return x * Y + y

for i in range(X):
	for j in range(Y):
		vertex.append([sys.maxsize, None])
		index = xy2index(i, j)
		unvisited.append(index)
		values.append(int(data[i][j]))

vertex[0][0] = 0

def get_next():
	candidate_id = None
	candidate_val = sys.maxsize

	for u in unvisited:
		if vertex[u][0] <= candidate_val:
			candidate_id = u
			candidate_val = vertex[u][0]

	return candidate_id

def get_adjusted(i):
	arr = []

	col = i % Y
	row = i // X

	if col + 1 < Y:
		arr.append(xy2index(row, col+1))
	if col - 1 >= 0:
		arr.append(xy2index(row, col-1))
	if row + 1 < X:
		arr.append(xy2index(row+1, col))
	if row - 1 >= 0:
		arr.append(xy2index(row-1, col))

	return arr	


while True:
	current_v = get_next()
	if current_v == None:
		break
	for next_v in get_adjusted(current_v):
		if vertex[next_v][0] > vertex[current_v][0] + values[next_v]:
			vertex[next_v][0] = vertex[current_v][0] + values[next_v]
			vertex[next_v][1] = current_v
	unvisited.remove(current_v)
	visited.append(current_v)

print(vertex.pop()[0])