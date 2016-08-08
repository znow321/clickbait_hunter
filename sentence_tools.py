from database import database
from utils import cls, error


def update_sentence_db():
    sentence = database.sentence
    if in_conflict():
        resolve_conflicts()
    database.database['sentences'][sentence] = database.clb_status
    cls()


def resolve_conflicts():  #  = conflicting status
    sentence = database.sentence
    cls()
    choice = get_answer()
    if choice == 'y':
        database.clb_status = database.clb_status


def in_database(): 
    sentence = database.sentence
    return sentence in database.database['sentences']


def in_conflict():
    clb_status = database.clb_status
    sentence = database.sentence
    if in_database():
        return database.database['sentences'][sentence] != clb_status
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
    clb_status = database.clb_status
    sentence = database.sentence
    status = ('clickbait', 'non-clickbait')
    if clb_status: 
        status = status[::-1]
    sentence = 'Do you wan\'t to toggle the "%s" sentence status' \
    ' from %s to %s?\n(Y/N)' % (sentence, status[0], status[1])
    return sentence
