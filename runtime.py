from manual_training import route 
from utils import init_save_dir
from database import database


# Most of other modules won't work without the database class
# It looks like the static database class method variables are shared between classes regardless where they are imported.


init_save_dir()


def start_identifier(sentence): # THIS IS THE ABSOLUTELY FIRST FUNCTION TO CALL 
    database.sentence = sentence
    route()


start_identifier("Hello this is me!")
