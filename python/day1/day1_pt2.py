entries = []

def add_entries_to_array():
	with open('input.txt') as file:
		for line in file:
			entries.append(int(line.strip()))

def find_two_entries():
	add_entries_to_array()
	for x in range(0, len(entries)):
		for y in range(x  + 1, len(entries)):
			for z in range(y +1, len(entries)):
				if entries[x] + entries[y] + entries[z] == 2020:
					print('Product of {} and {} and {}: {}'.format(entries[x], entries[y], entries[z], entries[x] * entries[y] * entries[z]))

if __name__ == '__main__':
	find_two_entries()
