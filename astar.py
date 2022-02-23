import csv

with open('dis_reta.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)
    # print(data)


# Grafo de conexões
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


# Retorna o custo real entre um estado e outro
def calculate_state_cost(current_state, next_station):
    for connection in range(0, len(connections[current_state - 1])):
        if connections[current_state - 1][connection][0] == next_station[0]:
            return connections[current_state - 1][connection][1]

        # Retorna se é necessário trocar de linha


def check_change_line(destination, line):
    for station_line in lines_in_stations[destination - 1]:
        if station_line == line:
            return False
    return True


# Retorna primeira linha em comum encontrada entre duas estações
def common_line(first_station, second_station):
    for first_station_lines in lines_in_stations[first_station - 1]:
        for second_station_lines in lines_in_stations[second_station - 1]:
            if first_station_lines == second_station_lines:
                return first_station_lines


def a_star_algorithm(start_point, end_point):
    # Variavel para checar se chegou ao fim
    is_finished = False
    border = []

    # Adicionando o ponto de partida na nossa lista de prioridades
    border.append(start_point)

    # Setando o custo para chegar no estado inicial para 0
    lower_cost_path[start_point[0] - 1][start_point[1]] = 0

    # Loop que itera enquanto a lista nao for vazia e ainda nao tivermos chegado ao fim
    while len(border) > 0 and not is_finished:

        # Seta o estado atual para o primeiro elemento da lista
        current_state = border.pop(0)

        # Checa se o estado atual é o estado final
        if current_state[0] == end_point[0]:
            is_finished = True

            if current_state[1] != end_point[1]:
                best_path[current_state[0] - 1][end_point[1]] = [current_state[0], current_state[1]]
                lower_cost_path[current_state[0] - 1][current_state[1]] += 0.0666667
                lower_cost_path[current_state[0] - 1][end_point[1]] = lower_cost_path[current_state[0] - 1][current_state[1]]



        else:
            # Itera por todas as conexões do estado atual
            for connection in connections[current_state[0] - 1]:

                # Inicializa a linha com a linha do estado atual
                actual_line = current_state[1]

                # Checa se será necessária uma mudança de linha
                change_line = check_change_line(connection[0], current_state[1])

                change_line_cost = 0
                # Se for necessario uma mudança de linha, atualiza o custo de mudança p 4 e atualiza a linha para a
                # linha que o estado atual e essa conexão tem em comum
                if (change_line):
                    change_line_cost = 0.0666667
                    actual_line = common_line(current_state[0], connection[0])

                # Calcula a heuristica referente a essa conexao
                h = data[connection[0] - 1][end_point[0] - 1]

                # Calcula o custo real referente a essa conexao
                cost = lower_cost_path[current_state[0] - 1][current_state[1]] + calculate_state_cost(current_state[0],
                                                                                         connection) + change_line_cost

                # Se o custo real calculado para chegar a esse estado for menor que se tem armazenado(ou se não
                # tiver sido calculado previamente), atualiza-se ele
                if (lower_cost_path[connection[0] - 1][actual_line] == -1) or (cost <= lower_cost_path[connection[0] - 1][actual_line]):

                    # Atualiza menor custo real para esse estado
                    lower_cost_path[connection[0] - 1][actual_line] = cost

                    if (change_line):
                        best_path[connection[0] - 1][actual_line] = [current_state[0], actual_line]
                        best_path[current_state[0] - 1][actual_line] = [current_state[0], current_state[1]]

                    else:
                        # Atualiza o estado que leva a esse estado com esse menor custo
                        best_path[connection[0] - 1][actual_line] = [current_state[0], current_state[1]]

                    # Insere na nossa lista em ordem o estado (conexao, linha)
                    counter = -1
                    inserted = False

                    # Itera pelos elementos na nossa lista
                    for station in border:
                        counter = counter + 1

                        # Checa se a soma (valor real + heuristica) do estado que desejamos inserir é menor que essa
                        # mesma soma do elemento atual da lista
                        if (lower_cost_path[connection[0] - 1][actual_line] +
                                float(h) <= lower_cost_path[station[0] - 1][station[1]] +
                                data[station[0] - 1][end_point[0] - 1]):
                            border.insert(counter, [connection[0], actual_line])
                            inserted = True
                            break

                    # Se não tiver inserido, insere no fim
                    if (not inserted):
                        border.insert(counter + 1, [connection[0], actual_line])


def main():
    time_connections()
    direct_time()

    a_star_algorithm((6, "blue"), (13, "red"))
    paths = read_path((13, "red"))
    for path in paths:
        print(f'E {str(path[0])} na linha {path[1]}')
    print(f'Tempo gasto: {str(lower_cost_path[12]["red"])} horas')


if __name__ == "__main__":
    main()