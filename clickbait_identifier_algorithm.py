from re import findall
import pickle
from os import system, path, makedirs
from time import sleep
from glob import glob


cls = lambda: system('cls')

#Creates save directory with a .gitignore if it's not already there
if not path.exists("clickbait_database"):  
	makedirs("clickbait_database")
	create_gitignore = open("clickbait_database\\.gitignore", "w")
	create_gitignore.write("*\n!.gitignore")
	create_gitignore.close()


def error(message, sleep_time=0):	
	cls()
	print(message)
	sleep(sleep_time)
	cls()

	
class Database_storage:
	database = []
	
	def __init__(self):
		Database_storage.database = self.import_database()
	
	def database_exists(self):
		return glob('clickbait_database\\database.pickle')
	
	def import_database(self):
		if self.database_exists():
			database_reader = open('clickbait_database\\database.pickle', 'r')
			database = database_reader.read()
			database_reader.close()
	
	def update_database(self):
		pass
	
	#If the sentence is flagged as clickbait
	def analyze(self,sentence):  
		lowercase_words = re.findall('[a-z\']*', sentence)
		uppercase_words = re.findall('[A-Z][a-z\']*', sentence)
		numbers = re.findall('[0-9]+', sentence)

	#User asking cycle
	def is_clickbait(self,sentence):
		while True:
			if self.user_menu(sentence):
				break

	def user_menu(self, sentence):
		cls()
		ask_user = 'Do you think "%s" sounds like clickbait?' \
					'\n\n1 - YES\n2 - NO\n3 - I WILL LET YOU DECIDE' \
					'\n\nPlease enter a number corresponding to your answer: '
		try:
			answer = int(input(ask_user % (sentence)))
			if answer not in [ 1, 2, 3 ]:
				raise ValueError
			return answer
		except ValueError:
			error('Invalid value entered, please try again...', 1)
			
x = Database_storage()
x.is_clickbait('XD')
