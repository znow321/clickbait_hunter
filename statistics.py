from sentence_tools import update_sentence_db 
from re import findall
# from statistics import mean  #  Will be implemented later
from database import database


def report_gen():
    # [ lowercase, upper_start, upper, number]  
    sentence = database.sentence
    templates = (r'\b[a-z\']+\b',r'\b[A-Z][a-z\']+\b',r'\b[A-Z\']+\b',r'\b[0-9]+\b')
    for template in templates:
        yield len(findall(template, sentence))


def percentages(sentence = database.sentence): # For both global & current 
    report = report_len()
    percent_per_word = 100 / report[0]
    for word_type in report[1:]:
        yield word_type * percent_per_word


def update_statistics_db():
    wordcount = list(report_gen()) 
    database.database['statistics']['num_lower'] = wordcount[0]
    database.database['statistics']['num_upper_start'] = wordcount[1]
    database.database['statistics']['num_upper'] = wordcount[2]
    database.database['statistics']['num_int'] = wordcount[3]
