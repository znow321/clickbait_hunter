from database import database


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


def resolve_conflicts():  #  = conflicting status
    clb_status = database.clb_status
    choice = get_answer()
    if choice == 'y':
        return not clb_status
    elif choice == 'n':
        return clb_status


def get_answer(): # Asking cycle
    clb_status = database.clb_status
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
