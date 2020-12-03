from functools import reduce

results = []
list_of_paths = []
deviations = [dict(right=1, down=1), dict(right=3, down=1), dict(right=5, down=1), dict(right=7, down=1),  dict(right=1, down=2)]

with open('input.txt') as f:
	for line in f:
		list_of_paths.append(list(line.strip()))

path_max_size = len(list_of_paths[0]) - 1


def multiple_slopes(slope_deviation, down_deviation):
	actual_position = 0
	total_amount_of_trees = 0

	for path in list_of_paths:
		if path == list_of_paths[0]:
			actual_position += slope_deviation
		elif down_deviation > 1:
			if list_of_paths.index(path) % 2 != 0:
				pass
			else:
	                        position = path[actual_position]
	                        if position == '#':
        	                        total_amount_of_trees += 1
                	        if (actual_position + slope_deviation) > path_max_size:
                        	        overlap = ((actual_position + slope_deviation) - path_max_size) - 1
                                	actual_position = overlap
	                        else:
        	                        actual_position += slope_deviation
		else:
			position = path[actual_position]
			if position == '#':
				total_amount_of_trees += 1
			if (actual_position + slope_deviation) > path_max_size:
				overlap = ((actual_position + slope_deviation) - path_max_size) - 1
				actual_position = overlap
			else:
				actual_position += slope_deviation

	results.append(total_amount_of_trees)


for deviation in deviations:
	multiple_slopes(deviation['right'], deviation['down'])

print(reduce(lambda x, y: x*y, results))
