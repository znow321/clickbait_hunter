from word_tools import increase_weight, decrease_weight
from sentence_tools import update_sentence_db
from utils import database


def identify(): # If the user is not sure
    wordcount_percentage = percentages()
    global_percentage = percentages()


def analyze():  # AFTER IDENTIFYING
    clb_status = database.clb_status
    if clb_status:  
        increase_weight() # Word update('words')
    else:
        decrease_weight()  # Word update('words')
    update_sentence_db()  # Sentence update('sentences') 
