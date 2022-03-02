import functools

f = open("input.txt", "r")
raw_data = f.read()
map_o = map(lambda x: int(x), raw_data.split("\n"))
data = list(map_o)

counter = 0;
prev_value = None;

for i in range(len(data)):
    if i < 3:
        continue

    a = data[i] + data[i-1] + data[i-2]
    b = data[i-1] + data[i-2] + data[i-3]
    

    if a > b:
        counter += 1

print(counter)