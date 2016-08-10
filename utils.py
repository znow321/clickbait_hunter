from os import path, system
from glob import glob
import platform
from time import sleep


class database: # Universal data storage function
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


def get_save_dir():
	return path.join('clickbait_database', 'database.sqlite')


#  Creates save directory with a .gitignore if it's not already there
def init_save_dir():
	if not path.exists('clickbait_database'):
		makedirs('clickbait_database')
        directory = path.join('clickbait_database','.gitignore'), 'w'
		create_gitignore = open(directory)
		create_gitignore.write('*\n!.gitignore')
		create_gitignore.close()


def database_exists():
	return glob(get_save_dir())


def word_database():
    return database.database['words']


def sentence_database():
    return database.database['sentences']
