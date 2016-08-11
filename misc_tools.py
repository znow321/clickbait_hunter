from word_tools import increase_weight, decrease_weight
from sentence_tools import update_sentence_db
from utils import db
from statistics import cur_ratio, global_avg_ratio, cur_weight, global_avg_weight


tolerated_limit = lambda value: value - db.error_tolerance


def identify(): # Once this returns, user check comes in. 
    total_score = 0 # Max 100%

    if db.sentence in sentence_db():
        return sentence_db()[db.sentence]
    else:
        for cur, globl in zip(cur_ratio(), global_avg_ratio()):
            if cur_ratio >= tolerated_limit(globl):
               total_score += 12.5 
        if cur_weight() >= tolerated_limit(global_avg_weight()):
            total_score += 50

    if total_score < 75:
        return False
    else:
        return True
    

def analyze():  # AFTER IDENTIFYING
    if db.clb_status:  
        increase_weight() # Word update('words')
    else:
        decrease_weight()  # Word update('words')
    update_sentence_db()  # Sentence update('sentences') 
