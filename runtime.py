#! /usr/bin/env python3

from utils import init_save_dir
from database_tools import db_load, db_save
from re import sub
from utils import db
from user_interface import route


init_save_dir()


def start_identifier(sentence, error_tolerance): # First func to call
    db_load()
    db.sentence = sub(r'[^A-Za-z0-9 ]', '', sentence)
    db.error_tolerance = error_tolerance
    route()
    db_save()
