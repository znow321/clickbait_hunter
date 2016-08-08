from sentence_tools import update_sentence_db 
from re import findall
# from statistics import mean  #  Will be implemented later
from database import database


# Only for temporary calculations


def lower(sentence = database.sentence):
    return len(findall(r'\b[a-z\']+\b', sentence))


def upper_start(sentence = database.sentence):
    return len(findall(r'\b[A-Z][a-z\']+\b', sentence))
    

def upper(sentence = database.sentence):
    return len(findall(r'\b[A-Z\']+\b',sentence))


def number(sentence = database.sentence):
    return len(findall(r'\b[0-9]+\b',sentence))


def update_statistics_db():
    database.database['statistics']['num_lower'] = lower()
    database.database['statistics']['num_upper_start'] = upper_start()
    database.database['statistics']['num_upper'] = upper()
    database.database['statistics']['num_int'] = number()


def percentages(sentence = database.sentence): # For both global & current 
    report = report_len()
    percent_per_word = 100 / report[0]
    for word_type in report[1:]:
        yield word_type * percent_per_word


def global_avg_ratio():
    global_ratio = [ 0, 0, 0, 0 ]
    for sentence, clb_status in database.database['sentences'].items():
       global_stats[0] += lower(sentence)
       global_stats[1] += upper_start(sentence)
       global_stats[2] += upper(sentence)
       global_stats[3] += number(sentence)
    return global_ratio


def global_avg_weight():
    global_weight = 0
    for sentence, clb_status in database.database['sentences'].items():
        for word in sentence.split():
            pass
