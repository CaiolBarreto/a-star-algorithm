def filter_distances(file, array: list):
    with open(file, 'r') as distances:
        aux_array = []
        for line in distances.readlines():
            remove_break = line.replace('\n', '')
            if not remove_break:
                copy = aux_array.copy()
                array.append(copy)
                aux_array.clear()
            else:
                aux_array.append(remove_break)


distances_list = []
filter_distances('lineDistances.txt', distances_list)
heuristic_table = {}
for number in range(1, 15):
    heuristic_table[f'E{number}'] = {}
for subway in range(1, 15):
    actual_list = distances_list[subway - 1]
    counter = 0
    for vertex in range(subway, 15):
        heuristic_table[f'E{subway}'][f'E{vertex}'] = actual_list[counter]
        heuristic_table[f'E{vertex}'][f'E{subway}'] = actual_list[counter]
        counter += 1
print(heuristic_table)

