#! /usr/bin/env python3

from utils import cls, sentence_db
from misc_tools import analyze, identify
from utils import db, error


def route():
    choice = get_choice()
    if choice == 1:
        database.clb_status = True
        analyze()
    elif choice == 2:
        database.clb_status = False
        analyze()
    elif choice == 3:
        auto()
    else:
        raise ValueError('Illegal value "%s" recieved!' % (choice))


def auto():
    if len(sentence_database()) == 0:
        error('Insufficient data for identifying!', 2)
    else:
        answer = identify()
        final_answer = user_confirmation(answer)
        if final_answer == 'n': 
            db.clb_status = not answer # Error here?
        else:
            db.clb_status = answer
        analyze()


def user_confirmation(clb_status):
    while True:
        cls()
        print(get_sentence())
        answer = input().lower()
        if answer not in ['y', 'n']:
            error('Invalid value entered, please try again...', 1)
        else:
            return answer


def get_sentence()
    if db.sentence not in sentence_db():
        status = 'is' if clb_status else "isn't"
        sentence = 'The clickbait identifier algorithm thinks the'  \
                   'sentence "%s" %s clickbait, ' \
                   'do you agree?\n(Y/N)' % (sentence, status)
    else:
        status = 'clickbait' if clb_status else 'non-clickbait'
        sentence = 'The sentence "%s" was confirmed by you as %s, ' \
                    'do you still agree?\n(Y/N)' % (sentence, status)
    return sentence


def get_choice(): 
    choice = 'Do you think "%s" sounds like clickbait?' \
             '\n\n1 - YES\n2 - NO\n3 - I\'LL LET YOU DECIDE' \
             '\n\nPlease enter a number ' \
             'corresponding to your answer: '
    while True:
        cls()
        try:
            answer = int(input(choice % (db.sentence)))
            if answer not in [ 1, 2, 3 ]:
                raise ValueError
            break
        except ValueError:
            error('Invalid value entered, please try again...', 1)
    return answer
