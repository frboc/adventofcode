from copy import deepcopy


def plot(map):
	for z in range(-2,4):
		print(z)
		for x in range(-1,5):
			for y in range(-1,5):
				point = (x, y, z)
				if point in map:
					print('#', end='')
				else:
					print('.', end='')
				# if point == (3,1,0):
				# 	print('<',end='')
			print()
		print()


def get_adjacent(x, y, z, w):
	adjacent = []
	for a in range(-1, 2):
		for b in range(-1, 2):
			for c in range(-1, 2):
				for d in range(-1, 2):
					if a == 0 and b == 0 and c == 0 and d == 0:
						continue
					adjacent.append((x+a, y+b, z+c, w+d))
	return adjacent


def count_active(points, map):
	counter = 0
	for point in points:
		if point in map:
			counter += 1

	return counter

def get_all_inactive(map):
	points = []

	for point in map:
		for adjacent_point in get_adjacent(*point):
			if not adjacent_point in map:
				points.append(adjacent_point)

	return set(points)



data = list(map(list, open("input.txt", "r").read().split('\n')))

map = {}
for x, row in enumerate(data):
	for y, char in enumerate(row):
		if char == '#':
			map[(x, y, 0, 0)] = True



for i in range(6):
	new_map = map.copy()

	for point in map:
		adjacent = get_adjacent(*point)
		active_adjacent = count_active(adjacent, map)

		if not active_adjacent in [2, 3]:
			del new_map[point]

	for point in get_all_inactive(map):
		adjacent = get_adjacent(*point)
		active_adjacent = count_active(adjacent, map)


		if active_adjacent == 3:
			new_map[point] = True
		

	map = new_map


res = len(map)
print(res)