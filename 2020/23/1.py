cups = [int(x) for x in open("input.txt", "r").read()]

def get_destination_value(cups, current_val):
    val = current_val
    while True:
        val -= 1
        if val in cups:
            return val
        if val == 0:
            val = 10


for i in range(100):
    source = cups.pop(0)
    picked = [cups.pop(0), cups.pop(0), cups.pop(0)]
    destination_key = cups.index(get_destination_value(cups, source))
    new_cups = []
    new_cups.extend(cups[:destination_key])
    new_cups.append(cups[destination_key])
    new_cups.extend(picked)
    new_cups.extend(cups[destination_key+1:])
    new_cups.append(source)
    cups = new_cups
    print(cups)

index_of_1 = cups.index(1)
cups_ordered = cups[index_of_1+1:]
cups_ordered.extend(cups[:index_of_1])

print(''.join(map(str, cups_ordered)))