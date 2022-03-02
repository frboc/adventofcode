import sys

f = open("input.txt", "r")
raw_data = f.read()
data = list(map(lambda x: int(x),raw_data.split(",")))

max_v = max(data)
min_cost = sys.maxsize

def magic(n):
	sum = 0
	for i in range(n+1):
		sum += i
	return sum

for i in range(max_v):
	cost = 0
	for val in data:
		cost += magic(abs(i - val))
		if cost > min_cost:
			break
	if cost < min_cost:
		min_cost = cost

print(min_cost)
