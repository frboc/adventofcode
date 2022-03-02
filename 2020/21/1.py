

data = []
all_alergens = []
for row in open("input.txt", "r").read().split('\n'):
	words, alergens = row[:-1].split(' (contains ')
	allergens = alergens.split(', ')
	
	all_alergens.extend(allergens)
	data.append((words.split(' '), alergens))

all_alergens = set(all_alergens)


all_alergens_sorted = []
for alergen in all_alergens:
	counter = 0
	for row in data:
		if alergen in row[1]:
			counter += 1

	all_alergens_sorted.append((counter, alergen))

all_alergens_sorted.sort(key=lambda x: x[0], reverse=True)





def get_with_alergen(alergen):
	res = []
	for row in data:
		if alergen in row[1]:
			res.append(row[0])
	return res

def get_common(list):
	common = []
	for el in list[0]:
		is_common = True
		for meal in list:
			if not el in meal:
				is_common = False
		if is_common:
			common.append(el)

	return common

while all_alergens_sorted:
	_, alergen = all_alergens_sorted.pop(0)
	meals = get_with_alergen(alergen)
	common_els = get_common(meals)

	for common_el in common_els:
		if not common_el:
			all_alergens_sorted.append((0, alergen))
			continue

		for meal, _ in data:
			if common_el in meal:
				meal.remove(common_el)


meals_left = []
for row in data:
	meals_left.extend(row[0])

res = len(meals_left)
print('part 1:', res)
assert res == 2265