f = open("input.txt", "r")
data = f.read().split("\n\n")

REQUIRED = ('byr','iyr','eyr','hgt','hcl','ecl','pid')


def is_valid(passport):
	for required_field in REQUIRED:
		if passport.find(required_field + ':') == -1:
			return False

	return True

counter = 0
for passport in data:
	if is_valid(passport):
		counter += 1


print(counter)
assert counter == 170
