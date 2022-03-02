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


max_number = 0
for code in data:
	result = row(code) * 8  + column(code)
	max_number = max(max_number, result)



print(max_number)
assert max_number == 883