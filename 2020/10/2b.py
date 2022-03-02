data = list(map(int, open("test_input.txt", "r").read().split("\n")))

data.append(max(data)+3)
max_data = max(data)