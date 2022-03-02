f = open("input.txt", "r")
data = list(map(lambda x: x.split(), f.read().split("\n\n")))



def is_valid(passport):
	counter = 0
	for param in passport:
		name, value = param.split(':')

		if name == 'byr' and 1920 <= int(value) <= 2002:
			counter += 1
		if name == 'iyr' and 2010 <= int(value) <= 2020:
			counter += 1
		if name == 'eyr' and 2020 <= int(value) <= 2030:
			counter += 1
		if name == 'hgt' and value[-2:] == 'cm' and 150 <= int(value[:-2]) <= 193:
			counter += 1
		if name == 'hgt' and value[-2:] == 'in' and 59 <= int(value[:-2]) <= 76:
			counter += 1
		try:
			if name == 'hcl' and value[0] == '#' and int(value[1:], 16):
				counter += 1
		except:
			pass
		if name == 'ecl' and value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
			counter += 1
		if name == 'pid' and len(value) == 9 and int(value):
			counter += 1

	if counter == 7:
		return True
	return False

counter = 0
for passport in data:
	if is_valid(passport):
		counter += 1


print(counter)
# assert counter == 170
