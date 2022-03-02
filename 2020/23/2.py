data = [int(x) for x in open("input.txt", "r").read()]

DATA_LEN = 1000000

def get_target(excluded, pointer):
    while True:
        pointer -= 1
        if pointer in excluded:
            continue
        if pointer == 0:
            pointer = DATA_LEN + 1
            continue
        return pointer


cups = {}
prev_val = DATA_LEN
for i in range(DATA_LEN):
    cups[prev_val] = data[i] if i < len(data) else i+1
    prev_val = cups[prev_val]
cups[prev_val] = data[0]
pointer = data[0]


for i in range(10000000):
    a = cups[pointer]
    b = cups[a]
    c = cups[b]
    # print(pointer, a, b, c)

    cups[pointer] = cups[c]

    target_num = get_target((a, b, c), pointer)
    # print('target', target_num, pointer)
    x = cups[target_num]
    cups[target_num] = a

    pointer = cups[pointer]

    cups[c] = x


    # print('asdf', pointer)
    # print(cups)




a = cups[1]
b = cups[a]
print(a, b)
res = a * b
print(res)
assert res == 511780369955