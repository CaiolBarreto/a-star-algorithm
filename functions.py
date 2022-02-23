import csv

CHANGE_STATION_TIME = 0.0666667

with open('distances.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)


connections = [
    [[2, 10]],
    [[1, 10], [3, 8.5], [9, 10], [10, 3.5]],
    [[2, 8.5], [4, 6.3], [9, 9.4], [13, 18.7]],
    [[3, 6.3], [5, 13], [8, 15.3], [13, 12.8]],
    [[4, 13], [6, 3], [7, 2.4], [8, 30]],
    [[5, 3]],
    [[5, 2.4]],
    [[4, 15.3], [5, 30], [9, 9.6], [12, 6.4]],
    [[2, 10], [3, 9.4], [11, 12.2]],
    [[2, 3.5]],
    [[9, 12.2]],
    [[8, 6.4]],
    [[3, 18.7], [4, 12.8], [14, 5.1]],
    [[13, 5.1]]
]

best_path = [
    {"blue": [-1, -1]},
    {"blue": [-1, -1], "yellow": [-1, -1]},
    {"blue": [-1, -1], "red": [-1, -1]},
    {"blue": [-1, -1], "green": [-1, -1]},
    {"blue": [-1, -1], "yellow": [-1, -1]},
    {"blue": [-1, -1]},
    {"yellow": [-1, -1]},
    {"yellow": [-1, -1], "green": [-1, -1]},
    {"yellow": [-1, -1], "red": [-1, -1]},
    {"yellow": [-1, -1]},
    {"red": [-1, -1]},
    {"green": [-1, -1]},
    {"green": [-1, -1], "red": [-1, -1]},
    {"green": [-1, -1]}
]

lines_in_stations = [
    ["blue"],
    ["blue", "yellow"],
    ["blue", "red"],
    ["blue", "green"],
    ["blue", "yellow"],
    ["blue"],
    ["yellow"],
    ["yellow", "green"],
    ["yellow", "red"],
    ["yellow"],
    ["red"],
    ["green"],
    ["green", "red"],
    ["green"]
]

lower_cost_path = [
    {"blue": -1},
    {"blue": -1, "yellow": -1},
    {"blue": -1, "red": -1},
    {"blue": -1, "green": -1},
    {"blue": -1, "yellow": -1},
    {"blue": -1},
    {"yellow": -1},
    {"yellow": -1, "green": -1},
    {"yellow": -1, "red": -1},
    {"yellow": -1},
    {"red": -1},
    {"green": -1},
    {"green": -1, "red": -1},
    {"green": -1}
]


def time_connections():
    for station in range(0, len(connections)):
        for connection in range(0, len(connections[station])):
            connections[station][connection][1] = connections[station][connection][1]/30


def direct_time():
    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            data[i][j] = float(data[i][j])/30


def read_path(end_point):
    current_state = end_point
    path = []
    path.append([end_point[0], end_point[1]])
    while best_path[current_state[0] - 1][current_state[1]][0] != -1:
        path.insert(0, best_path[current_state[0] - 1][current_state[1]])
        current_state = best_path[current_state[0] - 1][current_state[1]]
    return path


def calculate_state_cost(current_state, next_station):
    for connection in range(0, len(connections[current_state - 1])):
        if connections[current_state - 1][connection][0] == next_station[0]:
            return connections[current_state - 1][connection][1]


def check_change_line(destination, line):
    for station_line in lines_in_stations[destination - 1]:
        if station_line == line:
            return False
    return True
    

def common_line(first_station, second_station):
    for first_station_lines in lines_in_stations[first_station - 1]:
        for second_station_lines in lines_in_stations[second_station - 1]:
            if first_station_lines == second_station_lines:
                return first_station_lines
