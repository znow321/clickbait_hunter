from re import findall
import pickle
from os import system, path, makedirs
from time import sleep
from glob import glob


cls = lambda: system('cls')


if not path.exists("clickbait_database"):  #Creates database dir if it's not there
	makedirs("clickbait_database")
	create_gitignore = open("clickbait_database\\.gitignore", "w")
	create_gitignore.write("*\n!.gitignore")
	create_gitignore.close()

	
def database_exists():
	return glob('clickbait_database\\database.pickle')


def get_clickbait_database():  #Returns database it it's present
	if database_exists():
		database_reader = open('clickbait_database\\', 'r')
		database = database_reader.read()
		database_reader.close()
		return database


def update_database():
	pass


def analyze(sentence):
	lowercase_words = re.findall('[a-z\']*', sentence)
	uppercase_words = re.findall('[A-Z][a-z\']*', sentence)
	numbers = re.findall('[0-9]+', sentence)
	


def is_clickbait(sentence):  #User interface
	while True:
		cls()
		ask_user = 'Do you think "%s" sounds like clickbait?' \
					'\n\n1 - YES\n2 - NO\n3 - I WILL LET YOU DECIDE' \
					'\n\nPlease enter a number corresponding to your answer: '
		try:
			answer = int(input(ask_user % (sentence)))
			if answer not in [ 1, 2, 3 ]:
				raise ValueError
			break
		except ValueError:
			cls()
			print('Invalid value entered, please try again...')
			sleep(1)
			cls()


is_clickbait("You Won't believe")