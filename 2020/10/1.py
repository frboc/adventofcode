data = list(map(int, open("input.txt", "r").read().split("\n")))

data.append(0)
data.append(max(data)+3)
data.sort()
counters = [0, 0, 0]

for i, val in enumerate(data):
	if i == 0:
		continue
	if val - data[i-1] == 1:
		counters[0] += 1
	elif val - data[i-1] == 2:
		counters[1] += 1
	elif val - data[i-1] == 3:
		counters[2] += 1

print(counters)
result = counters[0] * counters[2]
print(result)
assert result == 1876