from database_tools import db_save, db_load
from word_tools import increase_weight, decrease_weight
from sentence_tools import
from logic_tools import identify
from utils import *


init_save_dir()


class database: # Universal data storage function
    sentence = ''
    tables = ('Words', 'Sentences', 'Statistics')
    database = {'Words':{},'Sentences':{},
                'Statistics':{'avg_lower':0, 
                'avg_start_upper':0, 
                'avg_upper':0, 'avg_num':0}}
    db_legacy = {}  #  Original copy for db item removal


def start_identifier(sentence): # THIS IS THE ABSOLUTELY FIRST FUNCTION YOU SHOULD CALL
    database.sentence = sentence
    route()
