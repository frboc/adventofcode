data = open("input.txt", "r").read().split("\n\n")



sum = 0
for group in data:
	MEMO = {}
	for ch in group.replace("\n", ""):
		MEMO[ch] = None
	sum += len(MEMO)

print(sum)
assert sum == 7027