from functions import lower_cost_path, CHANGE_STATION_TIME, best_path, connections, check_change_line, common_line, data, calculate_state_cost


def a_star_algorithm(start_point, end_point):
    is_finished = False
    border = []
    border.append(start_point)
    lower_cost_path[start_point[0] - 1][start_point[1]] = 0

    while len(border) > 0 and not is_finished:
        print(border)
        current_state = border.pop(0)
        if current_state[0] == end_point[0]:
            is_finished = True

            if current_state[1] != end_point[1]:
                best_path[current_state[0] - 1][end_point[1]] = [current_state[0], current_state[1]]
                lower_cost_path[current_state[0] - 1][current_state[1]] += CHANGE_STATION_TIME
                lower_cost_path[current_state[0] - 1][end_point[1]] = lower_cost_path[current_state[0] - 1][current_state[1]]
                
        else:
            for connection in connections[current_state[0] - 1]:
                actual_line = current_state[1]
                change_line = check_change_line(connection[0], current_state[1])
                change_line_cost = 0
                
                if (change_line):
                    change_line_cost = CHANGE_STATION_TIME
                    actual_line = common_line(current_state[0], connection[0])

                heurisitc_value = data[connection[0] - 1][end_point[0] - 1]
                cost = lower_cost_path[current_state[0] - 1][current_state[1]] + calculate_state_cost(current_state[0], connection) + change_line_cost

                if (lower_cost_path[connection[0] - 1][actual_line] == -1) or (cost <= lower_cost_path[connection[0] - 1][actual_line]):

                    lower_cost_path[connection[0] - 1][actual_line] = cost

                    if (change_line):
                        best_path[connection[0] - 1][actual_line] = [current_state[0], actual_line]
                        best_path[current_state[0] - 1][actual_line] = [current_state[0], current_state[1]]

                    else:
                        
                        best_path[connection[0] - 1][actual_line] = [current_state[0], current_state[1]]

                    counter = -1
                    inserted = False
                    
                    for station in border:
                        counter = counter + 1

                        if (lower_cost_path[connection[0] - 1][actual_line] +
                                float(heurisitc_value) <= lower_cost_path[station[0] - 1][station[1]] +
                                data[station[0] - 1][end_point[0] - 1]):
                            border.insert(counter, [connection[0], actual_line])
                            inserted = True
                            break

                    if (not inserted):
                        border.insert(counter + 1, [connection[0], actual_line])
        