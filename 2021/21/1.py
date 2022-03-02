f = open("input.txt", "r")
raw_data = f.read().split("\n")

dice = 0
rolls = 0
p = [int(list(raw_data[0])[-1]), int(list(raw_data[1])[-1])]
score = [0, 0]


def toss(player):
	global dice
	global rolls
	rolls += 1
	dice += 1
	if dice > 100:
		dice = 1
	return dice


while True:
	for i in range(3):
		p[0] += toss(0)

	x = p[0] % 10
	if x == 0:
		x = 10
	p[0] = x
	score[0] += x

	if score[0] >= 1000:
		break



	print(p[1])
	for i in range(3):
		p[1] += toss(1)

	x = p[1] % 10
	if x == 0:
		x = 10
	p[1] = x
	score[1] += x

	if score[1] >= 1000:
		break

loser = score[0] if score[0] < 1000 else score[1]
print(loser)
print(rolls)
print(rolls * loser)