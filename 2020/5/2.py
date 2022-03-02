f = open("input.txt", "r")
data = f.read().split("\n")


def row(code):
	num = ''
	for x in code[:7]:
		num += '1' if x == 'B' else '0'
	return int(num, 2)

def column(code):
	num = ''
	for x in code[-3:]:
		num += '1' if x == 'R' else '0'
	return int(num, 2)


occupied = {}
for code in data:
	occupied[(row(code), column(code))] = True


for row in range(128):
	for column in range(8):
		if not (row, column) in occupied and (row+1, column) in occupied and (row -1, column) in occupied:
			result = row * 8 + column
			print(result)
			assert result == 532
			exit()

