from database import database
from statistics import report_len
from sentence_tools import update_sentence_db
from word_tools import increase_weight, decrease_weight


def analyze():  # AFTER IDENTIFYING
    clb_status = database.clb_status
    if clb_status:  # Occurence count ('Statistics')
        update_statistics_db()
        increase_weight() # Word update('Words')
    else:
        decrease_weight()  # Word update('Words')

    update_sentence_db()  # Sentence update('Sentences') 

   
def update_statistics_db():
    wordcount = report_len() 
    stat_names = global_stat_names()
    for value, item in zip(wordcount, stat_names): 
        database.database['Statistics'][item] += value 


def global_stat_names():
    return [key for key, value in database.database['Statistics'].items()]
