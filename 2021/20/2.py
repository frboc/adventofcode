import copy
import math

f = open("input.txt", "r")
raw_data = f.read().split("\n")

key = raw_data[0]

old_img = []
for row in raw_data[2:]:
	old_img.append(list(map(lambda x: 1 if x == '#' else 0, list(row))))

start_img = copy.deepcopy(old_img)

def get_value(x, y, img_source):
	x -= MULTIPLIER
	y -= MULTIPLIER
	value = ''
	for i in range(-1, 2):
		for j in range(-1, 2):
			#print(x+i, y+j)
			try: 
				if x+i < 0 or y+j < 0:
					raise IndexError()
				value += str(img_source[x+i][y+j])
			except IndexError: 
				value += '0'
	#print(value)
	int_value = int(value, 2)
	char = key[int_value]
	return 1 if char == '#' else 0

# def get_middle(array, lenx, leny):
# 	a =  len(array) // 2 - lenx // 2
# 	b =  math.ceil(len(array) / 2) + math.ceil(lenx / 2)+1
# 	c =  len(array) // 2 - leny // 2
# 	d =  math.ceil(len(array) / 2) + math.ceil(leny / 2)+1

# 	new_arr = [[0] * leny]
# 	for row in array[a:b]:
# 		new_arr.append(row[c:d])
# 	return new_arr

MULTIPLIER = 5
STEPS = 50
for itr in range(STEPS):
	x = len(old_img) + MULTIPLIER * 2
	y = len(old_img[0]) + MULTIPLIER * 2
	new_img = [[0] * x for i in range(y)]

	for i in range(len(new_img)):
		for j in range(len(new_img[0])):
			new_img[i][j] = get_value(i, j, old_img)

	if itr % 2:
		filtered = []
		for row in new_img[8:-8]:
			filtered.append([])
			for ch in row[8:-8]:
				filtered[-1].append(ch)
		new_img = filtered
	#	new_img = get_middle(new_img, len(start_img) + 2 * (itr+1), len(start_img) + 2 * (itr+1))

	old_img = copy.deepcopy(new_img)




counter = 0
for row in new_img:
	print()
	for ch in row:
		counter += ch
		print('#' if ch else '.', end='')

print(counter)