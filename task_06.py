def rps_game_winner(l):
    #P - бумага
    #R - камень
    #S - ножницы

    check_list = ["P", "R", "S"]
    if len(l) != 2:
        raise "WrongNumberOfPlayersError"

    if l[0][1] not in check_list or l[1][1] not in check_list:
        raise "NoSuchStrategyError"

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

#rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])  #= > WrongNumberOfPlayersError
#rps_game_winner([['player1', 'P'], ['player2', 'A']])  #= > NoSuchStrategyError
print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))  #= > 'player2 S'
print(rps_game_winner([['player1', 'P'], ['player2', 'P']])) #=> 'player1 P'
print(rps_game_winner([['player1', 'S'], ['player2', 'P']]))