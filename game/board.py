# игровое поле / расстановка
import random


EMPTY = 0
SHIP = 1
BLOCKED = 2


def is_ship_fit(board, x_pos, y_pos, dx, dy, ln):
    for i in range(ln):
        if not( 0 <= y_pos <= 9 and 0 <= x_pos <= 9 ):
            return False

        for x_add in (-1, 0, 1):
            for y_add in (-1, 0, 1):
                if x_add == 0 and y_add == 0:
                    if board[y_pos][x_pos][1] in (SHIP, BLOCKED):
                        return False

                x_check, y_check = x_pos + x_add, y_pos + y_add
                if 0 <= x_check <= 9 and 0 <= y_check <= 9 \
                    and board[y_check][x_check][1] == SHIP:
                        return False

        y_pos += dy
        x_pos += dx

    return True


def place_ship(board: list, ln: int, idx: int) -> list:
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
                    else:
                        if 0 <= y_pos + y_add <= 9 and 0 <= x_pos + x_add <= 9:
                            if  board[y_pos + y_add][x_pos + x_add][1] == 0:
                                board[y_pos + y_add][x_pos + x_add][1] = 2

            x_pos += dx
            y_pos += dy

        return board

def create_empty_board() -> list:
    """
    Создаёт 2D-матрицу 10x10 - пустое игровое поле.
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

def init_board() -> list:
    """Создаёт поле и расставляет корабли."""
    board = create_empty_board()
    ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    for idx, ln in enumerate(ships):
        board = place_ship(board, ln, idx)

    return board

def render(board: list):
    alp = ("а", "б", "в", "г", "д",
            "е", "ё", "ж", "з", "и")

    print("   ", *[i for i in range(1, 11)], sep="  ")
    print("  ", "_" * 34, sep="")
    for i in range(10):
        print(alp[i], end=" ")
        print("|", *[j[0] for j in board[i]], "|", sep="  ")
    print("  ", "_" * 34, sep="")



# для тестов
def render_ships(board1: list):
    board = board1.copy()
    alp = ("а", "б", "в", "г", "д",
            "е", "ё", "ж", "з", "и")
    for i in range(10):
        for j in range(10):
            if board[i][j][1] == 1:
                board[i][j][0] = "@"
            if board[i][j][1] == 2:
                board[i][j][0] = ","
    print("   ", *[i for i in range(1, 11)], sep="  ")
    print("  ", "_" * 34, sep="")
    for i in range(10):
        print(alp[i], end=" ")
        print("|", *[j[0] for j in board[i]], "|", sep="  ")
    print("  ", "_" * 34, sep="")
