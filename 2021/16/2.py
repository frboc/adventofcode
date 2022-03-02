import functools

f = open("input.txt", "r")
data = f.read()

bits = []
for ch in data:
	xxx = bin(int(ch, 16))[2:].zfill(4)
	bits.append(xxx)
bits = "".join(bits)

pointer = 0

def eof():
	return bits[pointer:-1] == '' or int(bits[pointer:-1], 2) == 0

def peek(n, offset = 0):
	return bits[pointer+offset:pointer+offset+n]

def get_bits(n):
	global pointer
	text = bits[pointer:pointer+n]
	pointer += n
	return text

def parse_literal():
	pointer_start = pointer
	version = get_bits(3)
	type = get_bits(3)

	value = ''
	while True:
		val = get_bits(5)
		value += val[1:]
		if val[0] == '0':
			break

	return {
		'node_type': 'literal',
		'version': version,
		'length': pointer - pointer_start,
		'type': type,
		'value': int(value, 2),
	}

def get_length(nodes):
	length = 0
	for n in nodes:
		length += n['length']
	return length

def parse_operator():
	pointer_start = pointer
	version = get_bits(3)
	type = int(get_bits(3), 2)
	length_type = get_bits(1)
	length_bits = 11 if length_type == '1' else 15
	length = int(get_bits(length_bits), 2)

	end_of_packet = None
	if length_type == '0':
		end_of_packet = pointer + length

	inner_nodes = []
	while True:
		inner_nodes.append(parse_unknown())
		if length_type == '0' and get_length(inner_nodes) >= length:
			break
		if length_type == '1' and len(inner_nodes) >= length:
			break

	calculated_value = 0
	if (type == 0):
		calculated_value = functools.reduce(lambda a, b: a+b['value'], inner_nodes, 0)
	if (type == 1):
		calculated_value = functools.reduce(lambda a, b: a*b['value'], inner_nodes, 1)
	if (type == 2):
		calculated_value = min(map(lambda a: a['value'], inner_nodes))
	if (type == 3):
		calculated_value = max(map(lambda a: a['value'], inner_nodes))
	if (type == 5):
		calculated_value = 1 if inner_nodes[0]['value'] > inner_nodes[1]['value'] else 0
	if (type == 6):
		calculated_value = 1 if inner_nodes[0]['value'] < inner_nodes[1]['value'] else 0
	if (type == 7):
		calculated_value = 1 if inner_nodes[0]['value'] == inner_nodes[1]['value'] else 0

	return {
		'node_type': 'operator',
		'version': version,
		'length': pointer - pointer_start,
		'type': type,
		'inner_nodes': inner_nodes,
		'value': calculated_value
	}

def parse_unknown():
	packet_type = int(peek(3, 3), 2)
	if (packet_type == 4):
		return parse_literal()
	return parse_operator()

tree = []
while not eof():
	tree.append(parse_unknown())


def get_version_cumul(node):
	return node['value']

print(get_version_cumul(tree[0]))