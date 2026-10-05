from game.board import init_board, render
from game.clear_console import clear_console


EMPTY = 0
SHIP = 1
BLOCKED = 2

alpha = {'а':0, 'б':1, 'в':2, 'г':3, 'д':4, 'е':5, 'ж':6, 'з':7, 'и':8, 'к':9}
ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]


def win_text(count_turns):
    print(f" " * 13, "ПОБЕДА!")
    print(f" "*4, f"Вы произвели выстрелов: {count_turns}")
    print("\nНажмите Enter для перехода в меню")
    input()


def turn_check(request: str, board: list) -> (str, int):
    """
    Запрашивает координату у игрока до получения корректного ввода.

    Ввод считается корректным, если:
        * формат "<буква><число>"
        * число от 1 до 10, буква из "абвгдежзик"
        * клетка ещё не обстреляна ('.')

    :param request: текст для игрока
    :param board: игровое поле
    :return: корректная координата
    """
    while True:
        cell = input(request).replace(' ','').lower()

        if cell == "выход":
            return -1, -1

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


def game() -> None:
    """
    Основной игровой цикл морского боя.

    Запрашивает координаты хода, обрабатывает выстрел, обновляет поле
    и состояние кораблей, выводит результат. Завершается при уничтожении
    всех кораблей

    :return: None
    """
    # создание игрового поля с кораблями
    board, ships_positions = init_board()
    render(board)
    count_turns = 0 # количество сделанных ходов

    while True:
        #запрос координаты
        letter, digit = turn_check('Введите координату: ', board) #а2

        if letter == digit == -1:
            break

        count_turns += 1
        cell = board[alpha[letter]][digit - 1]

        #обработка хода
        hit_ship = 0 # 0 - мимо; 1 - попал; 2 - потопил
        if cell[1] != SHIP: # мимо
            cell[0] = '*'
        elif cell[1] == SHIP: # попал
            cell[0] = "X"
            ships[cell[2]] -= 1
            #если корабль уничтожен
            if ships[cell[2]] == 0: # потопил
                ship_destroyed(board, ships_positions[cell[2]])
                hit_ship = 2
            else:
                hit_ship = 1

        #обновление окна
        clear_console()
        render(board)
        if hit_ship == 0:
            print("Мимо!")
        elif hit_ship == 1:
            print("Попал!")
        elif hit_ship == 2:
            print("Потопил!")
            # если все корабли уничтожены
            if sum(ships) == 0:
                win_text(count_turns)
                break
