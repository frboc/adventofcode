import itertools
from collections import defaultdict


raw_data = open("input.txt", "r").read().split('\n')

data = []
for row in raw_data:
	if row == '':
		continue
	elif row[0:3] == '---':
		data.append([])
	else:
		data[-1].append(list(map(int, row.split(','))))


def flip(x, y, z, iterations):
	if iterations == 0:
		return (x, y, z)
	counter = 0
	for a, b, c in itertools.permutations([x, y, z]):
		for a2, b2, c2 in [(1,1,1),(1,1,-1),(1,-1,1),(-1,1,1),(1,-1,-1),(-1,-1,1),(-1,1,-1),(-1,-1,-1)]:
			val = (a*a2, b*b2, c*c2)
			counter += 1
			if counter == iterations:
				return val


def do_match(flip_id, current_scan):
	matching = defaultdict(int)
	for beacon in current_scan:
		beacon = flip(*beacon, flip_id)
		for mapped_b in MAP:
			a = mapped_b[0] - beacon[0]
			b = mapped_b[1] - beacon[1]
			c = mapped_b[2] - beacon[2]
			matching[(a, b, c)] += 1
			if (matching[(a, b, c)] >= 12):
				return (a, b, c)



MAP = set()
def add_to_map(beacons, flip_id, offset):
	for beacon in beacons:
		a, b, c = flip(*beacon, flip_id)
		x, y, z = offset
		MAP.add((a+x, b+y, c+z))


add_to_map(data[0], 0, (0,0,0))
data = data[1:]


while data:
	print(len(data))
	for beacon in data:
		for j in range(49):
			match = do_match(j, beacon)
			if match:
				print(match)
				add_to_map(beacon, j, match)
				data.remove(beacon)
				break
		if match:
			break

print(len(MAP))

