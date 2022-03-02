f = open("input.txt", "r")
raw_data = f.read()
data = raw_data.split("\n")

counter = 0;
prev_value = None;

for value in data:
    if (not prev_value):
        prev_value = value
        continue
    if (int(prev_value) < int(value)):
        counter += 1
    prev_value = value
        
print(counter)