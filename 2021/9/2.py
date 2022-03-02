import functools
import os
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

f = open("input.txt", "r")
data_raw = f.read()
data = data_raw.split('\n')


DIMENSION_X = len(data)
DIMENSION_Y = len(data[0])
res = []

def valid_index(i,j):
	if i < 0 or i >= DIMENSION_X or j < 0 or j >= DIMENSION_Y:
		return False
	return True

def get_adjusted(i, j):
	res = []
	if valid_index(i-1, j):
		res.append((i-1, j))
	if valid_index(i+1, j):
		res.append((i+1, j))
	if valid_index(i, j+1):
		res.append((i, j+1))
	if valid_index(i, j-1):
		res.append((i, j-1))
	return res


def magic(i, j):
	cur_value = data[i][j]
	for x in get_adjusted(i, j):
		if data[int(x[0])][int(x[1])] < cur_value:
			return
	return data[i][j]

def print_status():
	time.sleep(0.5)
	os.system('clear')
	for i in range(DIMENSION_X):
		print()
		for j in range(DIMENSION_Y):
			if (i, j) in bottom_list:
				print(bcolors.FAIL + str(data[i][j]) + bcolors.ENDC, end=' ')
			elif (i, j) in areas:
				print(bcolors.WARNING + str(data[i][j]) + bcolors.ENDC, end=' ')
			else:
				print(str(data[i][j]), end=' ')

res = []
bottom_list = []
for i in range(DIMENSION_X):
	for j in range(DIMENSION_Y):
		result = magic(i, j)
		if (result):
			res.append(int(result))
			bottom_list.append((i, j))


areas = []
for x in bottom_list:
	area = []
	area.append(x)

	loop = True
	while loop:
		loop = False
		for el in area:
			for el2 in get_adjusted(el[0], el[1]):
				if el2 in area:
					continue
				if data[el2[0]][el2[1]] == '9':
					continue
				area.append(el2)
				loop = True
	areas.append(area)
	#print_status()


areas.sort(key=lambda a: len(a), reverse=True)
print(areas)
print(len(areas[0]) * len(areas[1]) * len(areas[2]))
