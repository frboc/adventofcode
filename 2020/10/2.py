from collections import defaultdict

data = list(map(int, open("input.txt", "r").read().split("\n")))

data.append(max(data)+3)
max_data = max(data)

data = dict.fromkeys(data)

paths = [0]
counters = defaultdict(int)

while True:
	if not paths:
		break

	last_num = paths.pop(0)

	for i in (1,2,3):
		if last_num + i in data:
			if last_num+i not in paths:
				paths.append(last_num + i)
			counters[last_num+i] += max(1 , counters[last_num])


result = counters[max(data)]
print(result)

assert result == 14173478093824