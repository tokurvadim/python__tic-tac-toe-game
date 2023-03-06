def print_current_state_of_the_game():
    print("Текущее состояние игры:")
    print(f"{scheme_of_moves[0]} {scheme_of_moves[1]} {scheme_of_moves[2]}\n"
          f"{scheme_of_moves[3]} {scheme_of_moves[4]} {scheme_of_moves[5]}\n"
          f"{scheme_of_moves[6]} {scheme_of_moves[7]} {scheme_of_moves[8]}")


def move_by_x():
    print("Ход крестика.")
    current_move = int(input("Пожалуйста, введите цифру номера клетки от 1 до 9 для совершения хода:"))
    current_move -= 1
    if type(current_move) == int and current_move in range(0, 9) and (scheme_of_moves[current_move] == "-"):
        scheme_of_moves.pop(current_move)
        scheme_of_moves.insert(current_move, "x")
    else:
        print("Неверный ввод хода. Пожалуйста, попробуйте еще раз.")
        return move_by_x()


def move_by_0():
    print("Ход нолика.")
    current_move = int(input("Пожалуйста, введите цифру номера клетки от 1 до 9 для совершения хода:"))
    current_move -= 1
    if type(current_move) == int and (current_move in range(0, 9)) and (scheme_of_moves[current_move] == "-"):
        scheme_of_moves.pop(current_move)
        scheme_of_moves.insert(current_move, "0")
    else:
        print("Неверный ввод хода. Пожалуйста, попробуйте еще раз.")
        return move_by_0()


def check_winner_for_x():
    if ((scheme_of_moves[0] == 'x' and scheme_of_moves[4] == 'x' and scheme_of_moves[8] == 'x') or
            (scheme_of_moves[1] == 'x' and scheme_of_moves[4] == 'x' and scheme_of_moves[7] == 'x') or
            (scheme_of_moves[2] == 'x' and scheme_of_moves[4] == 'x' and scheme_of_moves[6] == 'x') or
            (scheme_of_moves[0] == 'x' and scheme_of_moves[1] == 'x' and scheme_of_moves[2] == 'x') or
            (scheme_of_moves[3] == 'x' and scheme_of_moves[4] == 'x' and scheme_of_moves[5] == 'x') or
            (scheme_of_moves[6] == 'x' and scheme_of_moves[7] == 'x' and scheme_of_moves[8] == 'x') or
            (scheme_of_moves[0] == 'x' and scheme_of_moves[3] == 'x' and scheme_of_moves[6] == 'x') or
            (scheme_of_moves[1] == 'x' and scheme_of_moves[4] == 'x' and scheme_of_moves[7] == 'x') or
            (scheme_of_moves[2] == 'x' and scheme_of_moves[5] == 'x' and scheme_of_moves[8] == 'x')):
        print("Игра окончена! Победили крестики. Финальное состояние игры:")
        print(f"{scheme_of_moves[0]} {scheme_of_moves[1]} {scheme_of_moves[2]}\n"
              f"{scheme_of_moves[3]} {scheme_of_moves[4]} {scheme_of_moves[5]}\n"
              f"{scheme_of_moves[6]} {scheme_of_moves[7]} {scheme_of_moves[8]}")
        return False
    else:
        print("Ход сделан.")
        return True


def check_winner_for_0():
    if ((scheme_of_moves[0] == '0' and scheme_of_moves[4] == '0' and scheme_of_moves[8] == '0') or
            (scheme_of_moves[1] == '0' and scheme_of_moves[4] == '0' and scheme_of_moves[7] == '0') or
            (scheme_of_moves[2] == '0' and scheme_of_moves[4] == '0' and scheme_of_moves[6] == '0') or
            (scheme_of_moves[0] == '0' and scheme_of_moves[1] == '0' and scheme_of_moves[2] == '0') or
            (scheme_of_moves[3] == '0' and scheme_of_moves[4] == '0' and scheme_of_moves[5] == '0') or
            (scheme_of_moves[6] == '0' and scheme_of_moves[7] == '0' and scheme_of_moves[8] == '0') or
            (scheme_of_moves[0] == '0' and scheme_of_moves[3] == '0' and scheme_of_moves[6] == '0') or
            (scheme_of_moves[1] == '0' and scheme_of_moves[4] == '0' and scheme_of_moves[7] == '0') or
            (scheme_of_moves[2] == '0' and scheme_of_moves[5] == '0' and scheme_of_moves[8] == '0')
            and check_for_draw()):
        print("Игра окончена! Победили нолики. Финальное состояние игры:")
        print(f"{scheme_of_moves[0]} {scheme_of_moves[1]} {scheme_of_moves[2]}\n"
              f"{scheme_of_moves[3]} {scheme_of_moves[4]} {scheme_of_moves[5]}\n"
              f"{scheme_of_moves[6]} {scheme_of_moves[7]} {scheme_of_moves[8]}")
        return False
    else:
        print("Ход сделан.")
        return True


def check_for_draw():
    if count_of_moves != 9:
        return True
    else:
        print("Игра окончена. Боевая ничья!")
        return False


def the_game():
    global count_of_moves
    count_of_moves = 0
    print("""Игра "Крестики-нолики". Перед началом объясним правила игры:\n
Участники по очереди ставят на свободные клетки поля знаки. Один играет крестиками, второй — ноликами. Обычно начинает
ходить участник, ставящий крестики. Выигрывает тот, кто первым выстроит в ряд 3 свои фигуры по вертикали, горизонтали или диагонали.\n
Правила выполнения хода: для выполнения хода необходимо ввести номер клетки, в которую Вы хотите поставить символ(крестик
или нолик.) Клетки имеют следующие номера:
1 2 3
4 5 6
7 8 9""")
    print("Начало игры. Обычно, первым ходит крестик.")
    print_current_state_of_the_game()
    while True:
        if check_for_draw():
            move_by_x()
            count_of_moves += 1
            if check_winner_for_x():
                print_current_state_of_the_game()
            else:
                break
        if check_for_draw():
            move_by_0()
            count_of_moves += 1
            if check_winner_for_0():
                print_current_state_of_the_game()
            else:
                break
        if check_for_draw():
            continue
        else:
            break

count_of_moves = None
scheme_of_moves = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
the_game()
