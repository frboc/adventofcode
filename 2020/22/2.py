a, b = open("input.txt", "r").read().split('\n\n')

deck1 = list(map(int, a.split('\n')[1:]))
deck2 = list(map(int, b.split('\n')[1:]))

MEMO_GLOBAL = {}

def play(deck1, deck2, dept = 0):
	if (tuple(deck1), tuple(deck2)) in MEMO_GLOBAL:
		return MEMO_GLOBAL[(tuple(deck1), tuple(deck2))]

	deck1_original = deck1
	deck2_original = deck2
	deck1 = deck1.copy()
	deck2 = deck2.copy()
	MEMO = {}

	i = 0
	while deck1 and deck2:
		i += 1
		if (tuple(deck1), tuple(deck2)) in MEMO:
			return ([1], [])
		MEMO[(tuple(deck1), tuple(deck2))] = True

		a = deck1.pop(0)
		b = deck2.pop(0)

		if a <= len(deck1) and b <= len(deck2):
			d1, d2 = play(deck1[:a], deck2[:b], dept + 1)
			is_winner_1 = bool(len(d1))
		else:
			is_winner_1 = a > b


		if is_winner_1:
			deck1.append(a)
			deck1.append(b)
		else:
			deck2.append(b)
			deck2.append(a)

	MEMO_GLOBAL[(tuple(deck1_original), tuple(deck2_original))] = (deck1, deck2)
	return (deck1, deck2)

deck1, deck2 = play(deck1, deck2)
winning_deck = deck1 if deck1 else deck2
winning_deck.reverse()
res = 0
for i, num in enumerate(winning_deck):
	i += 1
	res += num * i

print(res)
assert res == 35070