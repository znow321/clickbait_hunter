from os import path, system
from glob import glob
import platform
from time import sleep


get_save_dir = lambda: path.join('clickbait_database', 'database.sqlite')


git_dir = lambda: path.join('clickbait_database','.gitignore')


db_exists = lambda: glob(get_save_dir())


def word_db(): # For read-only operations
    return db.database['words']


def sentence_db(): # For read-only operations
    return db.database['sentences']


def db_legacy():
    return db.db_legacy


class db: # Universal data storage function
    sentence = ''
    clb_status = None
    error_tolerance = None
    tables = ('words', 'sentences')
    database = {'words':{},'sentences':{}}
    db_legacy = {}  #  Original copy for db item removal


def cls():
	if platform.system() == 'Linux':
			system('clear')
	elif platform.system() == 'Windows':
		system('cls')
	else:
		raise Exception('Shutting down, unknown operating system detected...')


def error(message, sleep_time=0):
	cls()
	print(message)
	sleep(sleep_time)
	cls()


#  Creates save directory with a .gitignore if it's not already there
def init_save_dir():
    if not path.exists('clickbait_database'):
        makedirs('clickbait_database')
        with open(git_dir(), 'w') as mk_git:
            mk_git.write('*\n!.gitignore')
