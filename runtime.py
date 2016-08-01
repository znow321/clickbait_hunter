from utils import init_save_dir


# Most of other modules won't work without the database class


init_save_dir()


class database: # Universal data storage function
    sentence = ''
    tables = ('Words', 'Sentences', 'Statistics')
    database = {'Words':{},'Sentences':{},
                'Statistics':{'avg_lower':0, 
                'avg_start_upper':0, 
                'avg_upper':0, 'avg_num':0}}
    db_legacy = {}  #  Original copy for db item removal


def start_identifier(sentence): # THIS IS THE ABSOLUTELY FIRST FUNCTION TO CALL 
    database.sentence = sentence
    route()
