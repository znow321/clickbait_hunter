from database import database
from statistics import update_statistics_db
from sentence_tools import update_sentence_db
from word_tools import increase_weight, decrease_weight


def analyze():  # AFTER IDENTIFYING
    clb_status = database.clb_status
    if clb_status:  # Occurence count ('statistics')
        update_statistics_db()
        increase_weight() # Word update('words')
    else:
        decrease_weight()  # Word update('words')

    update_sentence_db()  # Sentence update('sentences') 
