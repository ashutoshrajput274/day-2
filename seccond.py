def sum(a, b, c):
    return a + b + c


def printBoard(x, y):
    zero = 'x' if x[0] else ('o' if y[0]else 0)
    one = 'x' if x[1] else ('o' if y[1]else 1)
    two = 'x' if x[2] else ('o' if y[2]else 2)
    three = 'x' if x[3] else ('o' if y[3]else 3)
    four = 'x' if x[4] else ('o' if y[4]else 4)
    five = 'x' if x[5] else ('o' if y[5]else 5)
    six = 'x' if x[6] else ('o' if y[6]else 6)
    seven = 'x' if x[7] else ('o' if y[7]else 7)
    eight = 'x' if x[8] else ('o' if y[8]else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ")


def checkWin(x, y):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if (sum(x[win[0]], x[win[1]], x[win[2]]) == 3):
            print("Ashu won the match")
            return 1
        if (sum(y[win[0]], y[win[1]], y[win[2]]) == 3):
            print("Yashi won the match")
            return 0
    return -1


if __name__ == "__main__":
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for x and 0 for o
    print("welcome to my tic tac toe")
    while (True):
        printBoard(x, y)
        if (turn == 1):
            print("ashu turn")
            value = int(input("enter your value"))
            x[value] = 1
        else:
            print("yashi turn")
            value = int(input("enter a value"))
            y[value] = 1
        cwin = checkWin(x, y)
        if (cwin != -1):
            print("match over")
            break
        turn = 1-turn
