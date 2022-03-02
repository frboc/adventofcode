import functools

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

def magic(i, j):
	cur_value = data[i][j]

	if valid_index(i-1, j):
		if data[i-1][j] <= cur_value:
			return
	if valid_index(i+1, j):
		if data[i+1][j] <= cur_value:
			return
	if valid_index(i, j+1):
		if data[i][j+1] <= cur_value:
			return
	if valid_index(i, j-1):
		if data[i][j-1] <= cur_value:
			return
	return data[i][j]


res = []
res_map = []
for i in range(DIMENSION_X):
	for j in range(DIMENSION_Y):
		result = magic(i, j)
		if (result):
			res.append(int(result))
			res_map.append((i, j))

sum = 0
for x in res:
	sum += x + 1


for i in range(DIMENSION_X):
	print()
	for j in range(DIMENSION_Y):
		if (i, j) in res_map:
			print(bcolors.FAIL + str(data[i][j]) + bcolors.ENDC, end=' ')
		else:
			print(str(data[i][j]), end=' ')

print()
print(bcolors.WARNING + str(sum) + bcolors.ENDC)