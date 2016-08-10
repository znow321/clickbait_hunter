from utils import init_save_dir
from database_tools import db_load, db_save
from re import sub
from utils import database
from user_interface import route


init_save_dir()


def start_identifier(sentence, error_tolerance): # THIS IS THE ABSOLUTELY FIRST FUNCTION TO CALL 
    db_load()
    database.sentence = sub(r'[^A-Za-z0-9 ]', '', sentence)
    database.error_tolerance = error_tolerance
    route()
    exit_variable_dump()
    db_save()


def exit_variable_dump():
    print('Current sentence: %s' % (database.sentence))
    print('Clickbait status: %s' % (database.clb_status))
    print('Error tolerance: %s' % (database.error_tolerance))
    print('WORDS DATABASE DUMP')
    for key, value in database.database['words'].items():
        print('word: %s | weight: %s' % (key, value))
    print('SENTENCES DATABASE DUMP')
    for key, value in database.database['sentences'].items():
        print('sentence: %s | clickbait status: %s' % (key, value))
    print('DB LEGACY', end='')
    input(database.db_legacy)


start_identifier("This is a third ultimate sentence xd.", 1)
