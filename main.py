# здесь происходит управление всеми скриптами
from game.board import init_board, render, render_ship, render_ships1
from game.menu import main_menu
from game.clear_console import clear_console


while True:
    clear_console()
    main_menu()

    command = input("Введите команду: ").lower()
    if command in ("1", "играть"):
        print("game")
        board = init_board()
        render(board)
        input()
    elif command in ("2", "выход"):
        break
    elif command == "3":
        board = init_board()
        #render(board)
        render_ships1(board)
        input("Нажмите Enter для продолжения")

