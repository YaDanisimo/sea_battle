from game.board import render
from game.clear_console import clear_console


EMPTY = 0
SHIP = 1
BLOCKED = 2

alpha = {'а':0, 'б':1, 'в':2, 'г':3, 'д':4, 'е':5, 'ж':6, 'з':7, 'и':8, 'к':9}
ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]


def turn_check(request: str, board: list) -> (str, int):
    """
    Запрашивает координату у игрока до получения корректного ввода.

    Ввод считается корректным, если:
        * формат "<буква><число>"
        * число от 1 до 10, буква из 'абвгдежзик'
        * клетка ещё не обстреляна ('.')

    :param request: приглашение к вводу
    :param board: игровое поле
    :return: кортеж (буква, число) - валидная координата
    """
    while True:
        cell = input(request).replace(' ','').lower()
        if cell != "":
            cell_letter, cell_digit = cell[0], cell[1:]

            if cell_digit.isdigit() and cell_letter.isalpha():
                cell_digit = int(cell_digit)

                if 1 <= cell_digit <= 10 and cell_letter in 'абвгдежзик':
                    cell = board[alpha[cell_letter]][cell_digit - 1]

                    if cell[0] == '.':
                        return cell_letter, cell_digit

        print("! Неправильно указана координата !")


def ship_destroyed(board: list, ship_positions: list) -> None:
    """
    Закрашивает клетки, соседствующие с потопленным кораблём

    :param board: игровое поле
    :param ship_positions: позиции корабля на поле
    :return: None
    """
    for pos_y, pos_x in ship_positions:
        for x_add in (-1, 0, 1):
            for y_add in (-1, 0, 1):
                y, x = pos_y + y_add, pos_x + x_add
                if 0 <= y <= 9 and 0 <= x <= 9:
                    if board[y][x][0] == ".":
                        board[y][x][0] = "*"


def game(board: list, ships_positions: dict) -> None:
    """
    Основной игровой цикл морского боя.

    Запрашивает координаты хода, обрабатывает выстрел, обновляет поле
    и состояние кораблей, выводит результат. Завершается при уничтожении
    всех кораблей

    :param board: игровое поле
    :param ships_positions: позиции кораблей по их индексам
    :return: None
    """
    render(board)
    count_turns = 0

    while True:
        letter, digit = turn_check('Введите координату: ', board) #а2
        count_turns += 1
        cell = board[alpha[letter]][digit - 1]
        clear_console()
        hit_ship = 0 # 0 - мимо; 1 - попал; 2 - потопил
        if cell[1] != SHIP:
            cell[0] = '*'
        elif cell[1] == SHIP:
            cell[0] = "X"
            ships[cell[2]] -= 1
            if ships[cell[2]] == 0:
                ship_destroyed(board, ships_positions[cell[2]])
                hit_ship = 2
            else:
                hit_ship = 1

        render(board)
        if hit_ship == 0:
            print("Мимо!")
        elif hit_ship == 1:
            print("Попал!")
        elif hit_ship == 2:
            print("Потопил!")
            if  sum(ships) == 0:
                break
        if digit == 8:
            break
    print("\t\t\t ПОБЕДА!")
    print(f"\tВы произвели выстрелов: {count_turns}")
    print()
    print("Нажмите Enter для перехода в меню")
    input()