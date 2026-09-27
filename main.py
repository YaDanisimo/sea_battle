# здесь происходит управление всеми скриптами
from game.board import init_board, render, render_ships
from game.menu import main_menu
from game.clear_console import clear_console


while True:
    clear_console()
    main_menu()

    command = input("Введите команду: ").lower()
    if command in ("1", "играть"):
        print("game")
    elif command in ("2", "выход"):
        break
    elif command == "3":
        board = init_board()
        #render(board)
        render_ships(board)
        input("Нажмите Enter для продолжения")

