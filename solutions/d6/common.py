def calc_wins(time, distance):
    wins = []
    for time_held in range(time + 1):
        if time_held * (time - time_held) > distance:
            wins.append(time_held)

    return wins
