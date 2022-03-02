
import sys

f = open("input.txt", "r")
data = f.read().split('\n')

text = list(data[0])

rules = {}
for rule in data[2:]:
	x, y = rule.split(' -> ')
	rules[x] = y

STEPS = 10
for x in range(STEPS):
	print('step ' + str(x))
	offset = 0
	for index in range(len(text)):
		if index == 0:
			continue

		try:
			i = index + offset
			rule = text[i-1]+text[i]
		except IndexError:
			continue

		ch = rules[rule]
		text = text[:i] + [ch] + text[i:]
		offset += 1


counters = {}
for ch in text:
	if ch in counters:
		counters[ch] += 1
	else:
		counters[ch] = 0


val_min = sys.maxsize
val_max = 0
for key in counters:
	val = counters[key]
	val_min = min(val_min, val)
	val_max = max(val_max, val)


print(abs(val_min - val_max))


