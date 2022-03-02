from collections import deque
from copy import deepcopy

data = open("input.txt", "r").read().split('\n\n')

images = []
for img in data:
	title, *image = img.split('\n')
	images.append((int(title[5:9]), list(map(list, image))))

VERTEX_SIZE = int(len(images) ** (1/2))

def plot(img):
	print()
	for i in range(len(img)):
		for j in range(len(img[0])):
			print(img[i][j], end='')
		print()
	print()

def plot_whole_image(img):
	for a in range(len(img)):
		for i in range(len(img[0][0])):
			for b in range(len(img[0])):
				for j in range(len(img[0][0][0])):
					print(img[a][b][i][j], end='')
				# print('a', end='')
			print()
		print()
	print()
	exit()

def flip(img):
	new_img = [['' for i in range(len(img))]for i in range(len(img[0]))]

	for i in range(len(img[0])):
		for j in range(len(img)):
			new_img[i][j] = img[j][i]

	return new_img

def rotate(img):
	new_img = [['' for i in range(len(img))]for i in range(len(img[0]))]

	for i in range(len(img[0])):
		for j in range(len(img)):
			new_img[i][j] = img[j][-i-1]

	return new_img


def get_bottom_matching(el, pool):
	res = []
	for i, (label, img) in enumerate(pool):
		for _ in range(2):
			img = flip(img)
			for _ in range(4):
				img = rotate(img)
				if img[0] == el[-1]:
					res.append((i, label, img))

	return res


def get_column(start_fragment_id):
	images_pool = deepcopy(images)
	label, img = images_pool.pop(start_fragment_id)
	column_label = [label]
	column = [img]
	while len(column_label) < VERTEX_SIZE:
		matching = get_bottom_matching(column[-1], images_pool)

		if len(matching) > 1:
			return False

		if len(matching) == 0 and len(column) == 1:
			column = [rotate(column[0])]
			continue

		if len(matching) == 0:
			return False

		id, label, img = matching[0]
		column_label.append(label)
		column.append(img)
		images_pool.pop(id)

	return (column_label, column, images_pool)



for i in range(len(images)):
	column = get_column(i)
	if column:
		break


result_image = [list(map(lambda x: rotate(x), column[1]))]
result_image_label = [column[0]]
possible_results = [(result_image_label, result_image, column[2])]

def complete_image(labels, image, image_pool):
	rotated = False
	while image_pool:
		new_row = []
		new_row_label = []
		for el in image[-1]:
			matching = get_bottom_matching(el, image_pool)
			if len(matching) == 1:
				id, label, img = matching[0]
				image_pool.pop(id)
				new_row_label.append(label)
				new_row.append(img)
				continue

			if len(matching) > 1:
				print('asdf')
				exit()

		if len(new_row) == 0:
			if rotated:
				jreturn False
			rotated = True

			for i in range(len(image)):
				for j in range(len(image[0])):
					image[i][j] = rotate(rotate(image[i][j]))

			image = rotate(rotate(image))
			labels = rotate(rotate(labels))
			continue

		image.append(new_row)
		labels.append(new_row_label)

	return (labels, image)

for _ in range(1):
	possible_result = possible_results.pop(0)
	result = complete_image(*possible_result)
	if result:
		break

labels, img = result

res = labels[0][0] * labels[-1][-1] * labels[-1][0] * labels[0][-1]
assert res == 54755174472007
print('part 1: ', res)

def is_monster(x, y, image):
	monster = []
	monster.append('                  # ') 
	monster.append('#    ##    ##    ###')
	monster.append(' #  #  #  #  #  #   ')

	try:
		for a in range(len(monster)):
			for b in range(len(monster[0])):
				if monster[a][b] == '#' and image[x+a][y+b] != '#':
					return False
	except IndexError:
		return False

	return True


points_counter = 0
merged_image = []
for a in range(len(img)):
	for i in range(len(img[0][0])-1):
		if i == 0:
			continue
		merged_image.append([])
		for b in range(len(img[0])):
			for j in range(len(img[0][0][0])-1):
				if j == 0:
					continue
				if img[a][b][i][j] == '#':
					points_counter += 1
				merged_image[-1].append(img[a][b][i][j])



def count_monsters(merged_image):
	counter = 0
	for _ in range(2):
		merged_image = flip(merged_image)
		for _ in range(4):
			merged_image = rotate(merged_image)
			for x in range(len(merged_image)):
				for y in range(len(merged_image[0])):
					if is_monster(x, y, merged_image):
						counter += 1
			if counter > 0:
				return counter


MONSTER_LEN = 15
res = points_counter - count_monsters(merged_image) * MONSTER_LEN
print('part 2: ', res)
assert res == 1692