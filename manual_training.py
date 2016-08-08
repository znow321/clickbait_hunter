from database_tools import db_save, db_load
# from logic_tools import identify
from utils import *
from database import database
from analysis import analyze


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
        pass
        # identify()
    else:
        raise ValueError('Illegal value "%s" recieved!' % (choice))
