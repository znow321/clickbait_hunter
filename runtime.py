from utils import init_save_dir
from database_tools import db_load, db_save
from re import sub
from utils import database
from user_interface import route


init_save_dir()


def start_identifier(sentence): # THIS IS THE ABSOLUTELY FIRST FUNCTION TO CALL 
    db_load()
    database.sentence = sub(r'[^A-Za-z0-9 ]', '', sentence)
    route()
    db_save()


def exit_variable_dump():
    print('Current sentence: %s' % (database.sentence))
    print('Clickbait status: %s' % (database.clb_status))



start_identifier("This is a third ultimate sentence xd.")
