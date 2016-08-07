from sentence_tools import update_sentence_db 
from re import findall
# from statistics import mean  #  Will be implemented later
from database import database


def report_gen():
    # [ lowercase, upper_start, upper, number]  
    sentence = database.sentence
    yield findall(r'\b[a-z\']+\b', sentence)
    yield findall(r'\b[A-Z][a-z\']+\b', sentence)
    yield findall(r'\b[A-Z\']+\b', sentence)
    yield findall(r'\b[0-9]+\b', sentence)


def report_len():
    stats = list(report_gen())
    input(stats)
    return [len(word_type) for word_type in stats]


def percentages(sentence = database.sentence): # For both global & current 
    report = report_len()
    percent_per_word = 100 / report[0]
    for word_type in report[1:]:
        yield word_type * percent_per_word


def update_statistics_db():
    wordcount = report_len() 
    database.database['statistics']['num_lower'] = wordcount[0]
    database.database['statistics']['num_upper_start'] = wordcount[1]
    database.database['statistics']['num_upper'] = wordcount[2]
    database.database['statistics']['num_int'] = wordcount[3]
