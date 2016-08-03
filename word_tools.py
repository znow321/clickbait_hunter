from database import database


def increase_weight():
    sentence  = database.sentence 
    for word in sentence:
        if in_database(word):
            database.database['Words'][word] += 1
        else:
            database.database['Words'][word] = 1


def decrease_weight():
    sentence  = database.sentence 
    for word in sentence:
        if decrease_check(word):
            database.database['Words'][word] -= 1


def decrease_check(word):
    return in_database(word) and can_subtract(word)


def in_database(word):
    return word in database.database['Words']


def can_substract(word):
    return database.database['Words'][word] >= 1
