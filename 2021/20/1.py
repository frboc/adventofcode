import copy

f = open("input.txt", "r")
raw_data = f.read().split("\n")

key = raw_data[0]

old_img = []
for row in raw_data[2:]:
	old_img.append(list(map(lambda x: 1 if x == '#' else 0, list(row))))


MULTIPLIER = 10
x = len(old_img) + MULTIPLIER * 2
y = len(old_img[0]) + MULTIPLIER * 2
new_img = [[0] * x for i in range(y)]


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


for i in range(len(new_img)):
	for j in range(len(new_img[0])):
		new_img[i][j] = get_value(i, j, old_img)



for row in new_img:
	print()
	for ch in row:
		print('#' if ch else '.', end='')


print()

old_img = copy.deepcopy(new_img)
x = len(old_img) + MULTIPLIER * 2
y = len(old_img[0]) + MULTIPLIER * 2
new_img = [[0] * x for i in range(y)]

for i in range(len(new_img)):
	for j in range(len(new_img[0])):
		new_img[i][j] = get_value(i, j, old_img)


counter = 0
for row in new_img[15:-15]:
	print()
	for ch in row[15:-15]:
		counter += ch
		print('#' if ch else '.', end='')

print()
print(counter)