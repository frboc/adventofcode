from collections import Counter

f = open("input.txt", "r")
data = f.read().split('\n')

text = list(data[0])

rules = {}
for rule in data[2:]:
	x, y = rule.split(' -> ')
	rules[x] = y

STEPS = 40
counter = Counter()
for i in range(len(text)-1):
	counter[text[i]+text[i+1]] += 1
very_last_char = text[-1]


for i in range(STEPS):
	counter_copy = counter.copy()
	for (a, b) in counter_copy:
		new_ch = rules[a+b]
		multiplier = counter_copy[a+b]
		counter[a+new_ch] += multiplier
		counter[new_ch+b] += multiplier
		counter[a+b] -= multiplier

counter2 = Counter()
counter2[very_last_char] += 1

for key, val in counter.items():
	counter2[key[0]] += val

a = max(counter2.values())
b = min(counter2.values())
print(a - b)