tic_tac = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
           ]
def printer():
    print("---------")
    print("|", tic_tac[0][0], tic_tac[0][1], tic_tac[0][2], "|")
    print("|", tic_tac[1][0], tic_tac[1][1], tic_tac[1][2], "|")
    print("|", tic_tac[2][0], tic_tac[2][1], tic_tac[2][2], "|")
    print("---------")

printer()
no_draw = 0

def horizontal():
    for i in range(0, 3):
        for j in range(0, 1):
            if tic_tac[i][j] == tic_tac[i][j + 1] == tic_tac[i][j + 2] == " ":
                break
            elif tic_tac[i][j] == tic_tac[i][j + 1] == tic_tac[i][j + 2]:
                printer()
                print(tic_tac[i][j], "wins")
                global no_draw
                no_draw = 1
                break
            else:
                continue
        break


def vertical():
    for i in range(0, 3):
        for j in range(0, 1):
            if tic_tac[j][i] == tic_tac[j + 1][i] == tic_tac[j + 2][i] == " ":
                break
            elif tic_tac[j][i] == tic_tac[j + 1][i] == tic_tac[j + 2][i]:
                printer()
                print(tic_tac[j][i], "wins")
                global no_draw
                no_draw = 1
                break
            else:
                continue
        break


def diagonal():
    for i in range(0, 1):
        if tic_tac[i][i] == tic_tac[i + 1][i + 1] == tic_tac[i + 2][i + 2] == " ":
            break
        if tic_tac[i][i + 2] == tic_tac[i + 1][i + 1] == tic_tac[i + 2][i] == " ":
            break
        elif tic_tac[i][i] == tic_tac[i + 1][i + 1] == tic_tac[i + 2][i + 2] :
            printer()
            print(tic_tac[i][i], "wins")
            break
        elif tic_tac[i][i + 2] == tic_tac[i + 1][i + 1] == tic_tac[i + 2][i]:
            printer()
            print(tic_tac[i][i + 2], "wins")
            global no_draw
            no_draw = 1
            break
        else:
            break


def draw():
    if counter == 9 and no_draw == 0:
        print("Draw")


counter = 0

while counter < 9:
    x, y = input().split()
    try:
        tic_tac[int(x) - 1][int(y) - 1]
    except ValueError:
        print("You should enter numbers!")
    except IndexError:
        print("Coordinates should be from 1 to 3!")
    else:
        x = int(x) - 1
        y = int(y) - 1
        if tic_tac[x][y] == " ":
            if counter % 2 == 0:
                tic_tac[x][y] = "X"
                printer()
                counter += 1
                diagonal()
                horizontal()
                vertical()
                draw()
            else:
                tic_tac[x][y] = "O"
                printer()
                counter += 1
                diagonal()
                horizontal()
                vertical()
                draw()
        else:
            print("This cell is occupied! Choose another one!")
            continue
