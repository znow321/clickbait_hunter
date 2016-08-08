from manual_training import route 
from utils import init_save_dir
from database import database
from database_tools import db_save, db_load
from re import sub


init_save_dir()


def start_identifier(sentence): # THIS IS THE ABSOLUTELY FIRST FUNCTION TO CALL 
    db_load()
    database.sentence = sub(r'[^A-Za-z0-9 ]', '', sentence)
    route()
    db_save()


start_identifier("Hello there.")
