import random


EMPTY = 0
SHIP = 1
BLOCKED = 2

ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]


def is_ship_fit(board, pos_x, pos_y, dx, dy, ln):
    """
    Проверяет, можно ли разместить корабль заданной длины и направления,
    начиная с клетки (pos_x, pos_y), не задевая другие корабли и границы

    :param board: игровое поле (2д-матрица)
    :param pos_x: начальная координата X (горизонталь)
    :param pos_y: начальная координата Y (вертикаль)
    :param dx: смещение по X за шаг (0 или 1)
    :param dy: смещение по Y за шаг (0 или 1)
    :param ln: длина корабля
    :return: True, если размещение возможно, иначе False
    """
    for i in range(ln):
        if not( 0 <= pos_y <= 9 and 0 <= pos_x <= 9 ):
            return False

        for x_add in (-1, 0, 1):
            for y_add in (-1, 0, 1):
                if x_add == 0 and y_add == 0:
                    if board[pos_y][pos_x][1] in (SHIP, BLOCKED):
                        return False

                x_check, y_check = pos_x + x_add, pos_y + y_add
                if 0 <= x_check <= 9 and 0 <= y_check <= 9 \
                    and board[y_check][x_check][1] == SHIP:
                        return False

        pos_y += dy
        pos_x += dx

    return True


def place_ship(board: list, ln: int, idx: int) -> (list, list):
    """
    Ставит указанный корабль на поле, обновляет карту и
    записывает занятые им координаты в список

    :param board: Игровое поле (2д-матрица)
    :param ln: длина корабля
    :param idx: индекс корабля
    :return: список координат, на которых расположен корабль
    """
    ship_cords = []
    while True:
        vector = random.choice(["u", "r"])
        x_pos = random.randint(0, 9)
        y_pos = random.randint(0, 9)

        dx = 1 if vector == "r" else 0
        dy = 1 if vector == "u" else 0

        if not is_ship_fit(board, x_pos, y_pos, dx, dy, ln):
            continue

        for _ in range(ln):
            for x_add in (-1, 0, 1):
                for y_add in (-1, 0, 1):
                    if x_add == 0 and y_add == 0:
                        board[y_pos][x_pos][1] = 1
                        board[y_pos][x_pos][2] = idx
                        ship_cords.append((y_pos, x_pos))
                    else:
                        x, y = x_pos + x_add, y_pos + y_add
                        if 0 <= y <= 9 and 0 <= x <= 9:
                            if  board[y][x][1] == 0:
                                board[y][x][1] = 2

            x_pos += dx
            y_pos += dy

        return ship_cords


def create_empty_board() -> list:
    """
    Создаёт 2д-матрицу 10x10 - пустое игровое поле.
    Каждая ячейка представляет собой список из 3 элементов:
            Символ:
                    '.' - пустая клетка
                    'X' - подбитая часть корабля
                    '#' - область вокруг убитого корабля
            Тип клетки:
                    EMPTY = 0 - пустая клетка
                    SHIP = 1 - в клетке находится корабль
                    BLOCKED = 2 - пустая клетка рядом с кораблём
                            (в неё нельзя поставить другой корабль)
            Индекс корабля:
                    У каждого корабля есть индекс в массиве, начиная с 0
                            [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    Привязка клетки к индексу корабля нужна для определения состояния корабля
        жив / подбит / уничтожен
    Это определяется по количеству не подбитых клеток, которые привязаны к айди
    корабля.

    :return: 2D-матрица 10x10 с ячейками типа [Symbol, Type, Ship_index],
             где Symbol, Type и Ship_index по умолчанию равны '.', "EMPTY" и -1
    """
    board = []
    for i in range(10):
        board.append([[".", 0, -1] for _ in range(10)])
    return board


def init_board() -> (list, dict):
    """
    Создаёт поле, вызывает расстановку кораблей и
    связывает координаты кораблей с их индексами

    :return: игровое поле и словарь {индекс корабля: список координат}
    """
    board = create_empty_board()
    ships_positions = {}

    for idx, ln in enumerate(ships):
        ship_cords = place_ship(board, ln, idx)
        ships_positions[idx] = ship_cords

    return board, ships_positions


def render(board: list):
    """
    Выводит игровое поле таким, каким его должен видеть игрок

    :param board: игровое поле
    :return: None
    """
    alp = ("а", "б", "в", "г", "д",
            "е", "ж", "з", "и", "к")

    print("       ", *[i for i in range(1, 11)], sep=" ")
    print("      ", "=" * 23, sep="")

    for i in range(10):
        print("   ", alp[i], end=" ")
        print("|", *[j[0] for j in board[i]], "|", sep=" ")

    print("      ", "=" * 23, sep="")
