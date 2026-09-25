# здесь происходит управление всеми скриптами
from game.board import init_board, render
from game.menu import main_menu
from game.clear_console import clear_console


while True:
    clear_console()
    main_menu()
    player_command = input("Введите команду").lower()
    if player_command in ("1", "играть"):
        init_board()
        render()
        print("game start")
    elif player_command in ("2", "выход"):
        break
    else:
        print("Введена неверная команда")
