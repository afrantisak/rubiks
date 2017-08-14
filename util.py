def reverse_turn(turn):
    flip = {
        'F':  'Fi',
        'Fi': 'F',
        'R':  'Ri',
        'Ri': 'R',
        'L':  'Li',
        'Li': 'L',
        'U':  'Ui',
        'Ui': 'U',
        'D':  'Di',
        'Di': 'D',
        'B':  'Bi',
        'Bi': 'B',
    }
    if turn in flip:
        return flip[str(turn)]
    return turn


def reverse_move(move):
    move = reversed(move)
    move = [reverse_turn(turn) for turn in move]
    return move
