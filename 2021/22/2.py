
import re
import copy

f = open("input.txt", "r")
raw_data = f.read().split("\n")

class Cube:
	def __init__(self, on, x1, x2, y1, y2, z1, z2):
		self.on = on
		self.x1 = x1
		self.x2 = x2
		self.y1 = y1
		self.y2 = y2
		self.z1 = z1
		self.z2 = z2

	def get_size(self):
		a = self.x2 - self.x1 + 1
		b = self.y2 - self.y1 + 1
		c = self.z2 - self.z1 + 1
		return abs(a * b * c)


data = []
for row in raw_data:

	splited = re.split('[,.= ]', row)
	cube = Cube(True if splited[0] == 'on' else False, int(splited[2]), int(splited[4]), int(splited[6]), int(splited[8]), int(splited[10]), int(splited[12]))
	data.append(cube)

def overlap(cube1, cube2):
	if cube1.x1 > cube2.x2:
		return False
	if cube1.x2 < cube2.x1:
		return False
	if cube1.y1 > cube2.y2:
		return False
	if cube1.y2 < cube2.y1:
		return False
	if cube1.z1 > cube2.z2:
		return False
	if cube1.z2 < cube2.z1:
		return False
	return True

def get_overlaping_cube(cube1, cube2, on):
	x1 = max(cube1.x1, cube2.x1)
	x2 = min(cube1.x2, cube2.x2)
	y1 = max(cube1.y1, cube2.y1)
	y2 = min(cube1.y2, cube2.y2)
	z1 = max(cube1.z1, cube2.z1)
	z2 = min(cube1.z2, cube2.z2)

	return Cube(on, x1, x2, y1, y2, z1, z2)

cubes = []
for cube in data:
	for existing_cube in copy.deepcopy(cubes):
		if overlap(cube, existing_cube):
			on = None
			if existing_cube.on == True and cube.on == True:
				on = False
			elif existing_cube.on == False and cube.on == False:
				on = True
			elif existing_cube.on == True and cube.on == False:
				on = False
			elif existing_cube.on == False and cube.on == True:
				on = True

			cubes.append(get_overlaping_cube(cube, existing_cube, on))
	if cube.on:
		cubes.append(cube)



sum = 0
for cube in cubes:
	#print(cube.on, cube.get_size())
	if cube.on == True:
		sum += cube.get_size()
	else:
		sum -= cube.get_size()
print(sum)