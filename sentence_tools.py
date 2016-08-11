from utils import db, cls, error, sentence_db, word_db


def update_sentence_db():
    if in_conflict():
        resolve_conflicts()
    sentence_db()[db.sentence] = db.clb_status 
    # Overwrites the database entry ^


def resolve_conflicts():  #  = conflicting status
    cls()
    choice = get_answer()
    if choice == 'y':
        db.clb_status = db.clb_status # Not sure what does this do
    cls()


in_database = lambda: db.sentence in sentence_db()


def in_conflict():
    if in_database():
        return sentence_db()[db.sentence] != db.clb_status
    else:
        return False


def get_answer(): # Asking cycle
    while True:
        try:
            choice = input(get_question()).lower()
            assert(choice in ['y', 'n'])
            return choice
        except (ValueError, AssertionError):
            error('Invalid option entered, please try again...', 1)


def get_question(): 
    status = ('clickbait', 'non-clickbait')
    if db.clb_status: 
        status = status[::-1]
    sentence = 'Do you wan\'t to toggle the "%s" sentence status' \
    ' from %s to %s?\n(Y/N)' % (db.sentence, status[0], status[1])
    return sentence
