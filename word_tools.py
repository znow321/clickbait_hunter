from utils import db, word_db, sentence_db


def increase_weight():
    # Avoiding duplicates
    sentence  = sentence_split()
    if can_add(database.sentence):
        for word in sentence:
            if in_database(word):
                db.database['words'][word] += 1
            else:
                db.database['words'][word] = 1


def decrease_weight():
    sentence = sentence_split()
    for word in sentence:
        if decrease_check(word):
            db.database['words'][word] -= 1
        else:
            db.database['words'][word] = 0


def sentence_split():
    return db.sentence.split()


def in_database(word):
    return word in word_db()


def can_subtract(word):
    return word_db()[word] >= 1


def decrease_check(word):
    return in_database(word) and can_subtract(word)


def can_add(sentence):
    sentence_in_db = True
    try:
        sentence_false = sentence_db()[sentence] == False
    except KeyError:
        sentence_in_db = False
    if not sentence_in_db:
        return True
    elif sentence_false:
        return True
    else:
        return False
