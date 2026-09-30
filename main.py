from game.board import init_board
from game.menu import main_menu, rule_menu, creator_menu, donat_menu
from game.clear_console import clear_console
from game.game import game


while True:
    clear_console()
    main_menu()

    command = input().lower()
    clear_console()
    if command in ("1", "играть"):
        board, ships_positions = init_board()
        game(board, ships_positions)
    elif command in ("2", "правила"):
        rule_menu()
        input()
    elif command in ("3", "выход"):
        break
    elif command in ("4", "авторы"):
        creator_menu()
        input()
    elif command in ("5", "донат"):
        donat_menu()
        input()

