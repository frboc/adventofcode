f = open("input.txt", "r")

temp_sum = 0
all_sums = []
for row in f.read().split("\n"):
	if row == "":
		all_sums.append(temp_sum)
		temp_sum = 0
		continue
	temp_sum += int(row)

all_sums.sort(reverse=True)
part1 = all_sums[0]
print("Part 1: " + str(part1))
assert part1 == 75501


part2 = all_sums[0] + all_sums[1] + all_sums[2]
print("Part 2: " + str(part2))