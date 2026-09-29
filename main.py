# здесь происходит управление всеми скриптами
from game.board import init_board, render, render_ships, render_ships1
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
    elif command == "4":
        board = init_board()
        #render(board)
        render_ships1(board)
        input("Нажмите Enter для продолжения")
    elif command == "3":
        board = init_board()
        render_ships(board)
        input()
    elif command == "f":
        board = init_board()
        render(board)
        render_ships(board)
        render_ships1(board)
        input()

