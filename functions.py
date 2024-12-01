from random import choice


def spin_row():
    symbols = ['🍒', '🍉', '🍓', '🔔', '⭐']

    return [choice(symbols) for _ in range(3)]


def print_row(row):
    print(" | ".join(row))


def give_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        if row[0] == '🍉':
            return bet * 5
        if row[0] == '🍓':
            return bet * 7
        if row[0] == '🔔':
            return bet * 15
        if row[0] == '⭐':
            return bet * 25

    return 0
