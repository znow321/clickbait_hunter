from sentence_tools import update_sentence_db 
from re import findall
# from statistics import mean  #  Will be implemented later
from database import database


# [lower, upper_start, upper, num]


def lower(sentence = database.sentence):
    return len(findall(r'\b[a-z\']+\b', sentence))


def upper_start(sentence = database.sentence):
    return len(findall(r'\b[A-Z][a-z\']+\b', sentence))
    

def upper(sentence = database.sentence):
    return len(findall(r'\b[A-Z\']+\b',sentence))


def number(sentence = database.sentence):
    return len(findall(r'\b[0-9]+\b',sentence))


def percentages(sentence = database.sentence): # For both global & current 
    report = report_len()
    percent_per_word = 100 / report[0]
    for word_type in report[1:]:
        yield word_type * percent_per_word


def cur_ratio():
    cur_ratio = [ 0, 0, 0, 0 ]
    cur_ratio[0] = lower(sentence)
    cur_ratio[1] = upper_start(sentence)
    cur_ratio[2] = upper(sentence)
    cur_ratio[3] = number(sentence)
    return cur_ratio


def global_avg_ratio():
    global_ratio = [ 0, 0, 0, 0 ]
    for sentence, clb_status in database.database['sentences'].items():
       global_ratio[0] += lower(sentence)
       global_ratio[1] += upper_start(sentence)
       global_ratio[2] += upper(sentence)
       global_ratio[3] += number(sentence)
    return global_ratio


def cur_weight


def global_avg_weight():
    weight_list = [] # For final calculation
    for sentence, clb_status in database.database['sentences'].items():
        cur_weight = 0
        for word in sentence.split():
           cur_weight += database.database['words'][word] 
        weight_list.append(cur_weight)
    return sum(weight_list) / len(weight_list)
