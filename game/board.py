# игровое поле / расстановка
import random


def is_ship_fit(board, x_pos, y_pos, vector, ln):
    up = 0
    right = 0
    if vector == "u":
        up = 1
    elif vector == "r":
        right = 1

    for i in range(ln):
        if not( 0 <= y_pos <= 9 and 0 <= x_pos <= 9 ):
            return False
        for x_add in (-1, 0, 1):
            for y_add in (-1, 0, 1):
                x_check, y_check = x_pos + x_add, y_pos + y_add
                if x_add == 0 and y_add == 0:
                    if board[y_pos][x_pos][1] in (1, 2):
                        return False
                if 0 <= x_check <= 9 and 0 <= y_check <= 9 \
                    and board[y_check][x_check][1] == 1:
                        return False

        y_pos += up
        x_pos += right

    return True




def place_ship(board=list, ln=int, idx=int):
    ship_no_placed = True
    while ship_no_placed:
        vector = random.choice(["u", "r"])
        x_pos = random.randint(0, 9)
        y_pos = random.randint(0, 9)

        if is_ship_fit(board, x_pos, y_pos, vector, ln):
            up, right = 0, 0
            if vector == "u": up = 1
            elif vector == "r": right = 1

            for _ in range(ln):
                for x_add in (-1, 0, 1):
                    for y_add in (-1, 0, 1):
                        if x_add == 0 and y_add == 0:
                            board[y_pos][x_pos][1] = 1
                        else:
                            if 0 <= y_pos + y_add <= 9 and 0 <= x_pos + x_add <= 9:
                                if  board[y_pos + y_add][x_pos + x_add][1] == 0:
                                    board[y_pos + y_add][x_pos + x_add][1] = 2

                x_pos += right
                y_pos += up

            ship_no_placed = False

    return board


def init_ships(board=list) -> list:
    ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    for i in range(10):
        board = place_ship(board, ships[i], i)

    return board


def init_board() -> list: # новое игровое поле
    """
    Создаёт список 10x10 и случайно расставляет корабли,
    не ставя их вплотную друг к другу.

    :return: Список - игровое поле с расставленными кораблями
    """
    board = []
    for i in range(10):
            board.append([[".", 0] for _ in range(10)])
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

def render_ships(board1: list):
    board = board1.copy()
    alp = ("а", "б", "в", "г", "д",
            "е", "ё", "ж", "з", "и")
    for i in range(10):
        for j in range(10):
            if board[i][j][1] == 1:
                board[i][j][0] = "@"
    print("   ", *[i for i in range(1, 11)], sep="  ")
    print("  ", "_" * 34, sep="")
    for i in range(10):
        print(alp[i], end=" ")
        print("|", *[j[0] for j in board[i]], "|", sep="  ")
    print("  ", "_" * 34, sep="")
