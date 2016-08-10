from utils import cls, sentence_database
from misc_tools import analyze, identify
from utils import database, error


def get_choice(): 
    while True:
        cls()
        choice = 'Do you think "%s" sounds like clickbait?' \
                 '\n\n1 - YES\n2 - NO\n3 - I\'LL LET YOU DECIDE' \
                 '\n\nPlease enter a number ' \
                 'corresponding to your answer: '
        try:
            answer = int(input(choice % (database.sentence)))
            if answer not in [ 1, 2, 3 ]:
                raise ValueError
            break
        except ValueError:
            error('Invalid value entered, please try again...', 1)
    return answer


def route():
    choice = get_choice()
    if choice == 1:
        database.clb_status = True
        analyze()
    elif choice == 2:
        database.clb_status = False
        analyze()
    elif choice == 3:
        if len(sentence_database()) == 0:
            error('Insufficient data for identifying!', 2)
        else:
            answer = identify()
            final_answer = user_confirmation(answer)
            if final_answer == 'n': 
                database.clb_status = not answer # Error here?
            else:
                database.clb_status = answer
            analyze()
    else:
        raise ValueError('Illegal value "%s" recieved!' % (choice))


def user_confirmation(clb_status):
    status = 'is' if clb_status else "isn't"
    sentence = 'The clickbait identifier algorithm thinks the sentence "%s"' \
                ' %s clickbait, do you agree?\n(Y/N)' % (database.sentence,
                                                          status)
    while True:
        cls()
        print(sentence)
        answer = input().lower()
        if answer not in ['y', 'n']:
            error('Invalid value entered, please try again...', 1)
        else:
            return answer
