a, b = open("input.txt", "r").read().split('\n\n')

deck1 = list(map(int, a.split('\n')[1:]))
deck2 = list(map(int, b.split('\n')[1:]))


while deck1 and deck2:
	a = deck1.pop(0)
	b = deck2.pop(0)

	if a > b:
		deck1.append(a)
		deck1.append(b)
	else:
		deck2.append(b)
		deck2.append(a)


winning_deck = deck1 if deck1 else deck2
winning_deck.reverse()
res = 0
for i, num in enumerate(winning_deck):
	i += 1
	res += num * i

assert res == 33772
print(res)
