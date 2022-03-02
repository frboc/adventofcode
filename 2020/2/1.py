import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--test', action='store_true')
args = parser.parse_args()

if args.test:
	f = open("input.txt", "r")
else:
	f = open("test_input.txt", "r")

data = []
for row in f.read().split("\n"):
	data.append(row.split(' '))


def count_letter(text, char):
	counter = 0
	for ch in text:
		if (ch == char):
			counter += 1
	return counter


counter = 0
for rule, char, text in data:
	char = char.strip(':')
	min, max = list(map(int, rule.split('-')))

	if min <= count_letter(text, char) <= max:
		counter += 1

print(counter)



