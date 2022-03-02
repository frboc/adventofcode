from collections import deque
from copy import deepcopy

data = open("test_input.txt", "r").read().split('\n\n')

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


label, img = images.pop(0)
column_label = deque([label])
column = deque([img])
while len(column_label) < VERTEX_SIZE:
	if len(column_label) == 1:
		c = column.pop()
		column.append(rotate(c))

	label, img = images.pop(0)
	match = False
	for _ in range(2):
		img = flip(img)
		for _ in range(4):
			if match:
				break
			img = rotate(img)

			if img[0] == column[-1][-1]:
				column_label.append(label)
				column.append(img)
				match = True
				break

			if img[-1] == column[0][0]:
				column_label.appendleft(label)
				column.appendleft(img)
				match = True
				break

	if not match:
		images.append((label, img))

def get_bottom_matching(el, left_el = None):
	for i, (label, img) in enumerate(images):
		for _ in range(2):
			img = flip(img)
			for _ in range(4):
				img = rotate(img)

				if img[0] == el[-1]:
					if left_el:
						left = rotate(rotate(rotate(left_el)))
						right = rotate(el)
						if left[-1] != right[0]:
							continue

					images.pop(i)
					return (label, img)



map = [list(map(lambda x: rotate(x), column))]
map_label = [column_label]

while images:
	print(len(images))

	new_row = []
	new_row_label = []
	for el in map[-1]:
		left_el = new_row[-1] if len(new_row) > 0 else None
		new_piece = get_bottom_matching(el, left_el)
		if new_piece:
			new_row_label.append(new_piece[0])
			new_row.append(new_piece[1])

	if len(new_row) != 0:
		map.append(new_row)
		map_label.append(new_row_label)
	else:
		print(map_label)
		print()
		map = rotate(rotate(map))



res = map_label[0][0] * map_label[-1][-1] * map_label[-1][0] * map_label[0][-1]

print(res)