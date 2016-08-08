from utils import init_save_dir
from database_tools import db_load, db_save
from re import sub
from utils import database
from manual_training import route


init_save_dir()


def start_identifier(sentence): # THIS IS THE ABSOLUTELY FIRST FUNCTION TO CALL 
    db_load()
    database.sentence = sub(r'[^A-Za-z0-9 ]', '', sentence)
    route()
    db_save()


start_identifier("Hello there.")
