

#	 1   2   3   4   5   6   7   8   9   10  11  12   13  14
a = [1,	 1,  1,  26, 1,  1,  26, 1,  26, 1,  26,  26, 26, 26]
b = [15, 14, 11,-13, 14, 15, -7, 10, -12, 15, -16, -9, -8, -8]
c = [4,  16, 14, 3,  11, 13, 11, 7,  12,  15,  13,  1,  15, 4]

MEMO = {}



def magic(originalz, dept, num):
	i = dept
	w = num % 10
	z = originalz

	x = z % 26
	z = z // a[i]

	x += b[i]
	x = 0 if x == w else 1

	z *= 25 * x + 1
	y = (w + c[i]) * x

	z += y


	if b[i]<0 and z > originalz:
		return None


	if (z, dept) in MEMO:
		return None


	if dept == 13 and z != 0:
		print(num)
		return None
	if dept == 13 and z == 0:
		print('win', num)
		exit()


	for j in range(9, 0, -1):
		result = magic(z, dept+1, num*10 + j)
		if result:
			print('win', num*10+j)
			exit()
	MEMO[(z, dept)] = True


for j in range(9, 0, -1):
	magic(0, 0, j)
