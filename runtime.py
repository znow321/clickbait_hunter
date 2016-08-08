from manual_training import route 
from utils import init_save_dir
from database import database
from database_tools import db_save, db_load
from re import sub


# Most of other modules won't work without the database class
# It looks like the static database class method variables are shared between classes regardless where they are imported.


init_save_dir()


def start_identifier(sentence): # THIS IS THE ABSOLUTELY FIRST FUNCTION TO CALL 
    db_load()
    database.sentence = sub(r'[^A-Za-z0-9 ]', '', sentence)
    route()
    db_save()


start_identifier("Hello there.")
