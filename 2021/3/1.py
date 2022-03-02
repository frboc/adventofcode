f = open("input.txt", "r")
raw_data = f.read()
data = raw_data.split("\n")
x = [0] * 12

for row in data:
	for i in range(12):
		x[i] += 1 if row[i] == '1' else -1

res = ""
for i in range(12):
	res += '1' if x[i]>=0 else '0'

gama = int(res, 2)
epsilon = int(res, 2) ^ int('1'*12, 2)

print(gama * epsilon)
