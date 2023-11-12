def print_table(picks):
    print("---------")
    print("|", picks[0], picks[1], picks[2], "|")
    print("|", picks[3], picks[4], picks[5], "|")
    print("|", picks[6], picks[7], picks[8], "|")
    print("---------")


def check_win(picks):
    for i in range(0, 9, 3):
        if picks[i] == picks[i + 1] == picks[i + 2] != " ":
            return picks[i]

    for i in range(3):
        if picks[i] == picks[i + 3] == picks[i + 6] != " ":
            return picks[i]

    if picks[0] == picks[4] == picks[8] != " " or picks[2] == picks[4] == picks[6] != " ":
        return picks[4]

    if " " not in picks:
        return "Draw"

    return None


def move(picks, player):
    while True:
        try:
            x, y = map(int, input().split())

            if not (1 <= x <= 3 and 1 <= y <= 3):
                print("Coordinates should be from 1 to 3!")
                continue

            index = (x - 1) * 3 + (y - 1)

            if picks[index] == " ":
                picks[index] = player
                return
            else:
                print("This cell is occupied! Choose another one!")

        except ValueError:
            print("You should enter numbers!")


def tic_tac_toe_game():
    picks = [" "] * 9
    print_table(picks)
    player = "X"

    while True:
        move(picks, player)
        print_table(picks)
        result = check_win(picks)

        if result:
            if result == "Draw":
                print("Draw")
            else:
                print(result, "wins")
            break

        player = "O" if player == "X" else "X"


tic_tac_toe_game()
