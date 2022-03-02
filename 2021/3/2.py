f = open("input.txt", "r")
raw_data = f.read()

data = raw_data.split("\n")


def do_magic(data_copy):
	for i in range(12):
		x = 0
		for row in data_copy:
			x += 1 if row[i] == '1' else -1
		condition = '1' if x>=0 else '0'

		data_copy2 = data_copy.copy()
		for row in data_copy2:
			if row[i] != condition:
				data_copy.remove(row)
			if len(data_copy) == 1:
				return data_copy[0]

def do_magic2(data_copy):
	for i in range(12):
		x = 0
		for row in data_copy:
			x += 1 if row[i] == '1' else -1
		condition = '1' if x<0 else '0'

		data_copy2 = data_copy.copy()
		for row in data_copy2:
			if row[i] != condition:
				data_copy.remove(row)
			if len(data_copy) == 1:
				return data_copy[0]



res1 = do_magic(data.copy())
res2 = do_magic2(data.copy())

print(int(res1, 2) * int(res2, 2))
#6822109