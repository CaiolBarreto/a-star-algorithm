from functions import time_connections, direct_time, read_path, lower_cost_path
from a_star import a_star_algorithm


def main():
    time_connections()
    direct_time()

    a_star_algorithm((6, "blue"), (13, "red"))
    paths = read_path((13, "red"))
    for path in paths:
        print(f'E{str(path[0])} na linha {path[1]}')
    print(f'Tempo gasto: {float(lower_cost_path[12]["red"]):.2f} horas')


if __name__ == "__main__":
    main()