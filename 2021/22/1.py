
import re

f = open("input.txt", "r")
raw_data = f.read().split("\n")


data = []
for row in raw_data:

	splited = re.split('[,.= ]', row)
	cube = [splited[0], (int(splited[2]), int(splited[4])), (int(splited[6]), int(splited[8])), (int(splited[10]), int(splited[12]))]
	data.append(cube)


cube = {}
for i in range(-50, 51):
	cube[i] = {}
	for j in range(-50, 51):
		cube[i][j] = {}
		for k in range(-50, 51):
			cube[i][j][k] = 0

x = 0
for rule in data:
	x += 1
	print(str(x) + '/' + str(len(data)))
	for i in range(rule[1][0], rule[1][1]+1):
		if i < -50 or i > 50:
			continue
		#print(i)
		for j in range(rule[2][0], rule[2][1]+1):
			if j < -50 or j > 50:
				continue
			for k in range(rule[3][0], rule[3][1]+1):
				if k < -50 or k > 50:
					continue
				try:
					cube[i][j][k] = 1 if rule[0] == 'on' else 0
				except KeyError:
					pass

counter = 0
for i in range(-50, 50):
	for j in range(-50, 50):
		for k in range(-50, 50):
			if cube[i][j][k]:
				counter += 1

print(counter)

