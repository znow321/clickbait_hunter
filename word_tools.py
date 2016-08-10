from utils import database


def increase_weight():
    # Avoiding duplicates
    sentence  = sentence_split()
    if can_add(database.sentence):
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
        else:
            database.database['words'][word] = 0


def sentence_split():
    return database.sentence.split()


def in_database(word):
    return word in database.database['words']


def can_subtract(word):
    return database.database['words'][word] >= 1


def decrease_check(word):
    return in_database(word) and can_subtract(word)


def can_add(sentence):
    sentence_in_db = True
    try:
        sentence_false = database.database['sentences'][sentence] == False
    except KeyError:
        sentence_in_db = False
    if not sentence_in_db:
        return True
    elif sentence_false:
        return True
    else:
        return False
