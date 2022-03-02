f = open("input.txt", "r")
data = f.read()

bits = []
for ch in data:
	xxx = bin(int(ch, 16))[2:].zfill(4)
	bits.append(xxx)
bits = "".join(bits)

pointer = 0

def eof():
	return int(bits[pointer:-1], 2) == 0

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
	type = get_bits(3)
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

	return {
		'node_type': 'operator',
		'version': version,
		'length': pointer - pointer_start,
		'type': type,
		'inner_nodes': inner_nodes,
	}

def parse_unknown():
	packet_type  = peek(3, 3)
	if (int(packet_type, 2) == 4):
		return parse_literal()

	return parse_operator()

tree = []
while not eof():
	tree.append(parse_unknown())


def get_version_cumul(node):
	cumul = int(node['version'], 2)

	if node['node_type'] == 'operator':
		for literal in node['inner_nodes']:
			cumul += get_version_cumul(literal)
	return cumul

print(get_version_cumul(tree[0]))