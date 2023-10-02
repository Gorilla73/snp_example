class WrongNumberOfPlayersError(Exception):
    def __init__(self):
        self.__err = "WrongNumberOfPlayersError"

    def __str__(self):
        return self.__err


class NoSuchStrategyError(Exception):

    def __init__(self):
        self.__err = "NoSuchStrategyError"

    def __str__(self):
        return "NoSuchStrategyError"
def rps_game_winner(l):
    #P - бумага
    #R - камень
    #S - ножницы

    check_list = ["P", "R", "S"]
    try:
        if len(l) != 2:
            raise WrongNumberOfPlayersError
    except WrongNumberOfPlayersError:
        return WrongNumberOfPlayersError().__str__()

    try:
        if l[0][1] not in check_list or l[1][1] not in check_list:
            raise NoSuchStrategyError
    except NoSuchStrategyError:
        return NoSuchStrategyError().__str__()

    if l[0][1] == l[1][1]:
        return f"player1 {l[0][1]}"

    if l[0][1] == "P":
        if l[1][1] == "R":
            return "player1 P"
        else:
            return "player2 S"

    elif l[0][1] == "R":
        if l[1][1] == "P":
            return "player2 P"
        else:
            return "player1 R"

    else:
        if l[1][1] == "P":
            return "player1 S"
        else:
            return "player2 R"

print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))  #= > WrongNumberOfPlayersError
print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))  #= > NoSuchStrategyError
print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))  #= > 'player2 S'
print(rps_game_winner([['player1', 'P'], ['player2', 'P']])) #=> 'player1 P'
print(rps_game_winner([['player1', 'S'], ['player2', 'P']]))