from board import *
from clear_console import clear_console

EMPTY = 0
SHIP = 1
BLOCKED = 2

board = init_board()

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
# [".", SHIP, 0]
# ["X", SHIP, 3]
# [".", EMPTY, -1]

alpha = {'а':0, 'б':1, 'в':2, 'г':3, 'д':4, 'е':5, 'ё':6, 'ж':7, 'з':8, 'и':9}
ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

# print(alpha['г'])


def turn_check(promt: str, board):

    while True:
        kletka = input(promt).replace(' ','')

        cell_letter, cell_digit = kletka[0], kletka[1:]
        if cell_digit.isdigit() and cell_letter.isalpha():
            cell_digit = int(cell_digit)
            if 1 <= cell_digit <= 10 and cell_letter in 'абвгдеёжзи':
                cell = board[alpha[cell_letter]][cell_digit - 1]
                if cell[0] == '.':
                    return cell_letter, cell_digit

            # print("! Неправильно набрана клетка !")
        print("! Неправильно набрана клетка !")


def game(board: list):
    render(board)

    while True:
        letter, digit = turn_check('Введите клетку: ', board) #а2
        cell = board[alpha[letter]][digit - 1]
        clear_console()


        hit_ship = False
        if cell[1] != SHIP:
            cell[0] = '*'
        elif cell[1] == SHIP:
            hit_ship = True
            cell[0] = "X"
            ships[cell[2]] -= 1
        render(board)
        if hit_ship:
            print("Попал!")
        else:
            print("Мимо!")
game(board)








# turn_check('dssdf',[])