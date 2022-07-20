# write your code here
import random

user = "         "
tic_tac = []
row1 = [i for i in user[:3]]
tic_tac.append(row1)
row2 = [i for i in user[3:6]]
tic_tac.append(row2)
row3 = [i for i in user[6:]]
tic_tac.append(row3)

no_draw = 0
finish = 0


def printer():
    print("---------")
    print("|", tic_tac[0][0], tic_tac[0][1], tic_tac[0][2], "|")
    print("|", tic_tac[1][0], tic_tac[1][1], tic_tac[1][2], "|")
    print("|", tic_tac[2][0], tic_tac[2][1], tic_tac[2][2], "|")
    print("---------")


def horizontal():
    for i in range(0, 3):
        if tic_tac[i][0] == tic_tac[i][1] == tic_tac[i][2] == " ":
            break
        elif tic_tac[i][0] == tic_tac[i][1] == tic_tac[i][2]:
            print(tic_tac[i][0], "wins")
            global no_draw, finish
            finish = 1
            no_draw = 1
            break
        else:
            continue



def vertical():
    for i in range(0, 3):
        if tic_tac[0][i] == tic_tac[1][i] == tic_tac[2][i] == " ":
            break
        elif tic_tac[0][i] == tic_tac[1][i] == tic_tac[2][i]:
            print(tic_tac[0][i], "wins")
            global no_draw, finish
            no_draw = 1
            finish = 1
            break
        else:
            continue


def diagonal():
    for i in range(0, 1):
        if tic_tac[i][i] == tic_tac[i + 1][i + 1] == tic_tac[i + 2][i + 2] == " ":
            break
        if tic_tac[i][i + 2] == tic_tac[i + 1][i + 1] == tic_tac[i + 2][i] == " ":
            break
        elif tic_tac[i][i] == tic_tac[i + 1][i + 1] == tic_tac[i + 2][i + 2]:
            print(tic_tac[i][i], "wins")
            break
        elif tic_tac[i][i + 2] == tic_tac[i + 1][i + 1] == tic_tac[i + 2][i]:
            print(tic_tac[i][i + 2], "wins")
            global no_draw, finish
            no_draw = 1
            finish = 1
            break
        else:
            break


def draw():
    if counter == 9 and no_draw == 0:
        global finish
        finish = 1
        print("Draw")


def not_finished():
    if finish == 0:
        print("Game not finished")


def win_conditions():
    printer()
    diagonal()
    horizontal()
    vertical()
    draw()


printer()
player = "X"
counter = 0

while True:
    if player == "X":
        try:
            x, y = input("Enter the coordinates: ").split()
            tic_tac[int(x) - 1][int(y) - 1]
        except ValueError:
            print("You should enter numbers!")
        except IndexError:
            print("Coordinates should be from 1 to 3!")
        else:
            x = int(x) - 1
            y = int(y) - 1
            if tic_tac[x][y] == " ":
                if player == "X":
                    tic_tac[x][y] = "X"
                    counter += 1
                    win_conditions()
                    if finish == 1:
                        break
                    #not_finished()
                    player = "computer"
            else:
                print("This cell is occupied! Choose another one!")
                continue
    elif player == "computer":
        print('Making move level "easy"')
        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if tic_tac[x][y] == " ":
                tic_tac[x][y] = "O"
                break
            else:
                continue
        win_conditions()
        if finish == 1:
            break
        counter += 1

        #not_finished()
        player = "X"
