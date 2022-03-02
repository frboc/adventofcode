from itertools import permutations

f = open("input.txt", "r")
raw_data = f.read()
data = raw_data.split("\n")

MAP = ('abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg')

def decode(code):
	for i, x in enumerate(MAP):
		if (x == code):
			return i 

def sort(x: str):
	x = list(x)
	x.sort()
	return "".join(x)


def is_valid(vals, map):
	for word in vals:
		word = sort(word)

		new_word = translate(word, map)

		if (not sort(new_word) in MAP):
			return False

	return True

def translate(word, map):
	zipped = list(zip(map, ['a', 'b', 'c', 'd', 'e', 'f', 'g']))
	di = dict(zipped)

	word = sort(word)
	new_word = '';
	for ch in word:
		new_word += di[ch]

	return new_word


def magic(line):
	signal, out = line.split(' | ')
	out = out.split(' ');
	signal = signal.split(' ');

	asdf = signal.copy()
	asdf.extend(out)
	for map in permutations(['a', 'b', 'c', 'd', 'e', 'f', 'g']):
		if (is_valid(asdf, map)):
			break

	result = '';
	for x in out:
		translated = sort(translate(x, map))
		result += str(decode(translated))

	return int(result)

sum = 0
for x in data:
	sum += magic(x)

print(sum)