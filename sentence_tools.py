from database import database
from conflict_resolver import resolve_conflicts


def update_sentence_db():
    sentence = database.sentence
    clb_status = database.clb_status
    if can_automerge(): # TESTING HERE, POSSIBLE SEMANTIC ERROR
        clb_status = resolve_conflicts()
    database.database['sentences'][sentence] = clb_status


def in_database():
    clb_status = database.clb_status
    sentence = database.sentence
    return sentence in database.database['sentences']


def in_conflict():
    clb_status = database.clb_status
    sentence = database.sentence
    return database.database['sentences'][sentence] != clb_status


def can_automerge():
    sentence = database.sentence
    clb_status = database.clb_status
    return in_database() and not in_conflict()
