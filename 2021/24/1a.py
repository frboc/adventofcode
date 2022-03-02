

#	 1   2   3   4   5   6   7   8   9   10  11  12   13  14
a = [1,	 1,  1,  26, 1,  1,  26, 1,  26, 1,  26,  26, 26, 26]
b = [15, 14, 11,-13, 14, 15, -7, 10, -12, 15, -16, -9, -8, -8]
c = [4,  16, 14, 3,  11, 13, 11, 7,  12,  15,  13,  1,  15, 4]

for num in range(99999999999999, 11111111111111, -1):
	#num = 311612999999918
	if num % 100000 == 0:
		print(num)

	num = list(str(num))
	num.reverse()

	if '0' in num:
		continue

	z = 0
	y = 0
	x = 0
	w = 0
	for i in range(14):
		# w = int(num[i])
		# x = z
		# x = x % 26
		# z = int(z / a[i])
		# x += b[i]
		# x = 0 if x == w else 1
		# y = 25
		# y *= x
		# y += 1
		# z *= y
		# y = w
		# y += c[i]
		# y *= x
		# z += y


		w = int(num[i])
		x = z % 26 #x co je dole
		z = z // a[i] # z to co je nahore nebo vse

		x += b[i] # co bylo dole plus neco
		x = 0 if x == w else 1 # co bylo dole + neco == w pak dolu

		z *= 25 * x + 1
		y = (w + c[i]) * x

		z += y

		
		if z//26 == 0 and i > 0:
			print(i, num)
			exit()
	print(z)
	exit()


	if z == 0:
		print(num)
		exit()