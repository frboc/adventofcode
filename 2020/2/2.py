import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--test', action='store_true')
args = parser.parse_args()

if args.test:
	f = open("test_input.txt", "r")
else:
	f = open("input.txt", "r")

data = []
for row in f.read().split("\n"):
	data.append(row.split(' '))


counter = 0
for rule, char, text in data:
	char = char.strip(':')
	a, b = list(map(int, rule.split('-')))

	if text[a-1] != char and text[b-1] == char:
		counter += 1
	if text[a-1] == char and text[b-1] != char:
		counter += 1

print(counter)



