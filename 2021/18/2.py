import json
import math
import copy

f = open("input.txt", "r")
data_raw = f.read().split('\n')

data = list(map(lambda x: json.loads(x), data_raw))

def sum(x, y):
	return [copy.deepcopy(x), copy.deepcopy(y)]

def add_to_node(node, x, y):
	if x > 0 and not isinstance(node[0], list):
		node[0] += x + y
		return

	if Y > 0 and not isinstance(node[1], list):
		node[1] += x + y
		return

	res = []
	res.append(add_to_node(node[0], x, y))
	res.append(add_to_node(node[1], x, y))
	return res

def add_left(node, x):
	if not isinstance(node[0], list):
		node[0] += x
		return
	add_left(node[0], x)

def add_right(node, x):
	if not isinstance(node[1], list):
		node[1] += x
		return
	add_right(node[1], x)

def reduce(node):
	if not isinstance(node[0], list) and int(node[0]) >= 10:
		n = int(node[0])
		node[0] = [n//2, math.ceil(n/2)]
		return True

	if isinstance(node[0], list):
		if reduce(node[0]):
			return True

	if not isinstance(node[1], list) and int(node[1]) >= 10:
		n = int(node[1])
		node[1] = [n//2, math.ceil(n/2)]
		return True

	if isinstance(node[1], list):
		if reduce(node[1]):
			return True



def traverse(node, dept = 0):
	dept += 1
	if not isinstance(node, list):
		return node

	if dept == 5:
		c = node.copy()
		node = 0
		return c
	
	result = [0, 0]

	a = traverse(node[0], dept)
	if isinstance(a, list) and (a[0]>0 or a[1]>0):
		if isinstance(node[1], list):
			add_left(node[1], int(a[1]))
		else:
			node[1] = int(node[1]) + int(a[1])

		if dept == 4:
			node[0] = 0

		result[0] = a[0]
		if a[0] == 0:
			raise Exception('')

		return result

	b = traverse(node[1], dept)
	if isinstance(b, list) and (b[0]>0 or b[1]>0):
		if isinstance(node[0], list):
			add_right(node[0], int(b[0]))
		else:
			node[0] = int(node[0]) + int(b[0])


		if dept == 4:
			node[1] = 0

		result[1] = b[1]
		if b[1] == 0:
			raise Exception('')
		return result

def loop_traverse():
	prev = []
	while True:
		prev = copy.deepcopy(sumed)
		try:
			traverse(sumed)
		except Exception as error:
			pass
		#print('splited', sumed)
		if prev == sumed:
			break
	
def magnitude(node):
	if not isinstance(node, list):
		return int(node)

	return 3 * magnitude(node[0]) + 2* magnitude(node[1])
	

sumed = data[0]
#print('       ',sumed)	

prev = []
while True:
	prev = copy.deepcopy(sumed)
	loop_traverse()
	reduce(sumed)
	#print('reduced', sumed)
	if prev == sumed:
 		break



max_magnitude = 0.
for i in range(len(data)):
	for j in range(len(data)):
		for x in range(1):
			if x == 1:
				sumed = sum(data[i], data[j])
			else:
				sumed = sum(data[j], data[i])

			#print(sumed)

			prev = []
			while True:
				prev = copy.deepcopy(sumed)
				loop_traverse()
				reduce(sumed)
				#print('reduced', sumed)
				if prev == sumed:
					mag = magnitude(sumed)
					if max_magnitude < mag:
						max_magnitude = mag
					break


print(max_magnitude)
