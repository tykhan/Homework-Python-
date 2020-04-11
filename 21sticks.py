def make_move(sticks):
    if sticks<3:
        return sticks
    else:
        return sticks%4
        