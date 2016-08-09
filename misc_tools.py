from word_tools import increase_weight, decrease_weight
from sentence_tools import update_sentence_db
from utils import database


def identify(): # Once this returns, user check comes in. 
    cur_ratio = cur_ratio()
    global_avg_ratio = global_avg_ratio()

    cur_weight = cur_weight()
    global_avg_weight = global_avg_weight()

    sentence = database.sentence
    sentence_db = database.database['sentences']

    if sentence in sentence_db:
        return sentence_db[sentence]
    else:
        pass

    # Max points = 4xCell(4 - 50%) + Weight(50%) = 50 or 100 or 0
    # Or if analyzed respond directly ^^^ ( line 17 )
    

def tolerated_range(value):
    tolerance = database.tolerance
    return list( range(value - tolerance, value + tolerance))


def analyze():  # AFTER IDENTIFYING
    clb_status = database.clb_status
    if clb_status:  
        increase_weight() # Word update('words')
    else:
        decrease_weight()  # Word update('words')
    update_sentence_db()  # Sentence update('sentences') 
