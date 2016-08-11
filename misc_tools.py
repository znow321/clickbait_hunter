from word_tools import increase_weight, decrease_weight
from sentence_tools import update_sentence_db
from utils import db
from statistics import cur_ratio, global_avg_ratio, cur_weight, global_avg_weight


def identify(): # Once this returns, user check comes in. 
    cur_rtio = cur_ratio()
    global_avg_rtio = global_avg_ratio()

    cur_wght = cur_weight()
    global_avg_wght = global_avg_weight()

    sentence = db.sentence

    total_score = 0 # Max 100%

    if sentence in sentence_db():
        return sentence_db()[sentence]
    else:
        for cur, globl in zip(cur_rtio, global_avg_rtio):
            if cur_ratio >= tolerated_limit(globl):
               total_score += 12.5 
        if cur_wght >= tolerated_limit(global_avg_wght):
            total_score += 50

    if total_score < 75:
        return False
    else:
        return True
    

def tolerated_limit(value):
    tolerance = db.error_tolerance
    return value - tolerance


def analyze():  # AFTER IDENTIFYING
    clb_status = db.clb_status
    if clb_status:  
        increase_weight() # Word update('words')
    else:
        decrease_weight()  # Word update('words')
    update_sentence_db()  # Sentence update('sentences') 
