# здесь происходит управление всеми скриптами
from game.board_generator import board_generate
from game.menu import main_menu


while True:
    main_menu()
    player_command = input("Введите команду").lower()
    if player_command in ("1", "играть"):
        print("game start")
    elif player_command in ("2", "выход"):
        break
    else:
        print("Введена неверная команда")