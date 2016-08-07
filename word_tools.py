from database import database


def increase_weight():
    sentence  = sentence_split()
    for word in sentence:
        if in_database(word):
            database.database['words'][word] += 1
        else:
            database.database['words'][word] = 1


def decrease_weight():
    sentence = sentence_split()
    for word in sentence:
        if decrease_check(word):
            database.database['words'][word] -= 1


def sentence_split():
    return database.sentence.split()


def decrease_check(word):
    return in_database(word) and can_subtract(word)


def in_database(word):
    return word in database.database['words']


def can_substract(word):
    return database.database['words'][word] >= 1
