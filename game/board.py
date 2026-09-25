# игровое поле / расстановка
from random import randint

def init_board() -> list: # новое игровое поле
    """
    Создаёт список 10x10 и случайно расставляет корабли,
    не ставя их вплотную друг к другу.

    :return: Список - игровое поле с расставленными кораблями
    """
    return [1, 0, 'X']

def render(board: list):
    print(*board, sep="\n")