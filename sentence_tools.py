from database import database


def update_sentence_db():
    sentence = database.sentence
    clb_status = database.clb_status

    if not can_automerge():
        clb_status = resolve_conflicts(clb_status)
        database.database['Sentences'][sentence] = clb_status


def can_automerge():
    sentence = database.sentence
    clb_status = database.clb_status

    in_database = in_database(sentence, clb_status)
    in_conflict = in_conflict(sentence, clb_status)
    return in_database and not in_conflict


def in_database():
    clb_status = database.clb_status
    sentence = database.sentence
    return sentence in database.database['Sentences']


def in_conflict():
    clb_status = database.clb_status
    sentence = database.sentence
    return database.database['Sentences'][sentence] != clb_status
