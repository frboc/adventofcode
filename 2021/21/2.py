f = open("input.txt", "r")
raw_data = f.read().split("\n")

memo = {}


def combinations():
	res = []
	for x in range(1,4):
		for y in range(1,4):
			for z in range(1,4):
				res.append(x+y+z)
	return res

def get_winner_ratio(p, score, toss, player):
	global memo

	hash = str(p) +'-'+ str(score) +'-'+ str(toss)+str(player)
	if hash in memo:
		#print(hash, memo[hash])
		return memo[hash]

	p[player] = (p[player] + toss) % 10
	if p[player] == 0:
		p[player] = 10
	score[player] += p[player]
	if score[player] >= 21:
		#print(p[player], score[player], toss)
		w = [0, 0]
		w[player] = 1
		memo[hash] = w
		return w

	next_player = 1 if player == 0 else 0
	res = [0, 0]
	for toss in combinations():
		a = get_winner_ratio(p.copy(), score.copy(), toss, next_player)
		res[0] += a[0]
		res[1] += a[1]
	#res = [a[0] + b[0] + c[0], a[1] + b[1] + c[1]]
	#print(hash, res)
	memo[hash] = res
	return res



p = [int(list(raw_data[0])[-1]), int(list(raw_data[1])[-1])]
score = [0, 0]

res = [0, 0]
for toss in combinations():
	a = get_winner_ratio(p.copy(), score.copy(), toss, 0)
	res[0] += a[0]
	res[1] += a[1]


if res[0] > res[1]:
	print(res[0])
else:
	print(res[1])