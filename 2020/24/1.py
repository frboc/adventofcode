DIRECTIONS = {'e', 'w', 'se', 'sw', 'ne', 'nw'}
SPACE = set()

def parse(line):
	steps = []
	line = list(line)

	while line:
		ch = line.pop(0)
		if not ch in DIRECTIONS:
			ch += line.pop(0)
		steps.append(ch)

	return steps

def move(i, j, direction):
	if direction == 'e':
		return (i+1, j)
	elif direction == 'w':
		return (i-1, j)
	elif direction == 'se':
		return (i, j+1)
	elif direction == 'nw':
		return (i, j-1)
	elif direction == 'ne':
		return (i+1, j-1)
	elif direction == 'sw':
		return (i-1, j+1)
	else:
		raise

def get_adjacent(i, j):
	l = []
	for direction in DIRECTIONS:
		l.append(move(i, j, direction))

	assert len(l) == 6
	return l

def get_all_relevant_tiles(space):
	l = []
	for tile in space:
		l.extend(get_adjacent(*tile))
		l.append(tile)
	return set(l)

def count_adjacent_black(i, j, space):
	counter = 0
	for tile in get_adjacent(i, j):
		if is_black(*tile, space):
			counter += 1
	return counter

def is_black(i, j, space):
	return (i, j) in space


for row in open('input.txt', 'r').read().split('\n'):
	steps = parse(row)
	position = (0, 0)
	for step in steps:
		position = move(*position, step)

	if position in SPACE:
		SPACE.remove(position)
	else:
		SPACE.add(position)

print('part 1:', len(SPACE))
# assert len(SPACE) == 266


for i in range(100):
	NEW_SPACE = SPACE.copy()
	for tile in get_all_relevant_tiles(SPACE):
		if is_black(*tile, SPACE) and not count_adjacent_black(*tile, SPACE) in [1, 2]:
			NEW_SPACE.remove(tile)
		elif not is_black(*tile, SPACE) and count_adjacent_black(*tile, SPACE) == 2:
			NEW_SPACE.add(tile)

	SPACE = NEW_SPACE
print('part 2', len(SPACE))
asert len(SPACE) == 3627