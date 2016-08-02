from manual_training import route 
from utils import init_save_dir
from database_tools import db_save, db_load
from word_tools import increase_weight, decrease_weight
# from sentence_tools import
from logic_tools import identify

# Most of other modules won't work without the database class


init_save_dir()


class database: # Universal data storage function
    sentence = ''
    clb_status = False
    tables = ('Words', 'Sentences', 'Statistics', 'Stat_aux')
    database = {'Words':{},'Sentences':{},
                'Statistics':{'avg_lower':0, 
                'avg_start_upper':0, 
                'avg_upper':0, 'avg_int':0},
                'Stat_aux':{'num_lower':0,
                'num_start_upper':0,
                'num_upper':0,
                'num_int':0}}
    db_legacy = {}  #  Original copy for db item removal


def start_identifier(sentence): # THIS IS THE ABSOLUTELY FIRST FUNCTION TO CALL 
    database.sentence = sentence
    route()


start_identifier("Hello this is madness!")
input("Exiting")
