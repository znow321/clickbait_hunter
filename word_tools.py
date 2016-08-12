#! /usr/bin/env python3

from utils import db, word_db, sentence_db


in_database = lambda word: word in word_db()


can_subtract = lambda word: word_db()[word] >= 1


decrease_check = lambda word: in_database(word) and can_subtract(word)


sentence_split = lambda: db.sentence.split()


def increase_weight():
    # Avoiding duplicates
    if can_add(database.sentence):
        for word in sentence_split():
            if in_database(word):
                db.database['words'][word] += 1
            else:
                db.database['words'][word] = 1


def decrease_weight():
    for word in sentence_split():
        if decrease_check(word):
            db.database['words'][word] -= 1
        else:
            db.database['words'][word] = 0


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
