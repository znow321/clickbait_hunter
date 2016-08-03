

def resolve_conflicts():  #  = conflicting status
    clb_status = database.clb_status
    choice = get_answer(clb_status)
    if choice == 'y':
        return not clb_status
    elif choice == 'n':
        return clb_status


def get_answer(): # Asking cycle
    clb_status = database.clb_status
    while True:
        try:
            choice = input(get_question())
            assert(choice.lower() in ['y', 'n'])
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
    'from %s to %s?\n(Y/N)' % (sentence, status[0], status[1])
    
    return sentence
