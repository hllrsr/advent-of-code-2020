list_of_paths = []

with open('input.txt') as f:
	for line in f:
		list_of_paths.append(list(line.strip()))


actual_position = 0
path_max_size = len(list_of_paths[0]) - 1
total_amount_of_trees = 0

for path in list_of_paths:
	if path == list_of_paths[0]:
		actual_position += 3
	else:
		position = path[actual_position]
		if position == '#':
			total_amount_of_trees += 1
		if (actual_position + 3) > path_max_size:
			overlap = ((actual_position + 3) - path_max_size) - 1
			actual_position = overlap
		else:
			actual_position += 3

print(total_amount_of_trees)
