f = open("input.txt", "r")
data = f.read().split(",")

arr = [0] * 9

for fish in data:
	arr[int(fish)] += 1


for i in range(256):
	x = arr.pop(0)
	arr[6] += x
	arr.append(x)

print(sum(arr))