from re import findall
import pickle
from os import system, path, makedirs
from time import sleep
from glob import glob
from statistics import mean


cls = lambda: system('cls')


#  Creates save directory with a .gitignore if it's not already there
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


class DatabaseTools:
	#  Words - All together, Sentences - All together, Statistics - clickbait only
	database = {'words':{},'sentences':{},
				'statistics':{'avg_lower':0, 'avg_start_upper':0, 
				'avg_upper':0, 'avg_num':0}}
	
	def __init__(self):
		self._save_dir = 'clickbait_database\\database.pickle'
		self.load_database()
	
	def __database_exists(self):
		return glob(self._save_dir)
	
	def load_database(self):
		if self.__database_exists():
			database_loader = open(self._save_dir, 'rb')
			DatabaseTools.database = pickle.load(database_loader)
			database_loader.close()
	
	def save_database(self):
		database_saver = open(self._save_dir, 'wb')
		pickle.dump(DatabaseTools.database, database_saver)
		database_saver.close()


class WordTools:
	def decrease_check(self, word):
		in_database = word in DatabaseTools.database['words']
		can_subtract = DatabaseTools.database['words'][word] >= 1
		return in_database and can_subtract

	def increase_weight(self):
		for word in self.sentence:
			if word in DatabaseTools.database['words']:
				DatabaseTools.database['words'][word] += 1
			else:
				DatabaseTools.database['words'][word] = 1

	def decrease_weight(self):
		for word in self.sentence:
			if self.decrease_check(word):
				DatabaseTools.database['words'][word] -= 1


class SentenceTools:
	def can_automerge(self, clickbait_status):
		in_database = self.sentence in DatabaseTools.database['sentences']
		is_conflict = DatabaseTools.database['sentences'][self.sentence] != clickbait_status
		return in_database and not is_conflict

	def update_sentence_database(self, clickbait_status=True):
		if not self.can_automerge():
			clickbait_status = self.resolve_conflicts(clickbait_status)
		DatabaseTools.database['sentences'][self.sentence] = clickbait_status

	def resolve_conflicts(self, clickbait_status):  #  = conflicting status
		status = ('clickbait', 'non-clickbait')
		if clickbait_status: status = status[::-1]
		say = 'Do you wan\'t to toggle the "%s" sentence status' \
				'from %s to %s?\n(Y/N)' % (self.sentence, status[0], status[1])
		print(say)



class Logic:
	#  If the sentence is flagged as clickbait
	def analyze(self):
		total_words = len(self.sentence.split())
		lowercase_words = len(findall('[a-z\']*', self.sentence))
		uppercase_starting_words = len(findall('[A-Z][a-z\']*', self.sentence))
		uppercase_words = len(findall('[A-Z\']*', self.sentence))
		numbers = len(findall('[0-9]+', self.sentence))
		stats = percentage(total_words, lowercase_words, 
				uppercase_starting_words, uppercase_words, number)

	def percentage(self, total=0, lower=0, upper_start=0, upper=0, num=0):
		percent_per_word = 100 / total
		percent_lower = lower * percent_per_word
		percent_upper_start = upper_start * percent_per_word
		percent_upper = upper * percent_per_word
		percent_num = num * percent_per_word
		return [percent_lower, percent_upper_start, percent_upper, percent_num]


	def identify(self):
		pass


class ClickbaitIdentifierUI(Logic, WordTools, DatabaseTools, SentenceTools):
	def __init__(self, sentence):
		self.sentence = sentence

	def user_menu(self):
		while True:
			cls()
			choice = 'Do you think "%s" sounds like clickbait?' \
						'\n\n1 - YES\n2 - NO\n3 - I\'LL LET YOU DECIDE' \
						'\n\nPlease enter a number ' \
						'corresponding to your answer: '
			try:
				answer = int(input(choice % (self.sentence)))
				if answer not in [ 1, 2, 3 ]:
					raise ValueError
				break
			except ValueError:
				error('Invalid value entered, please try again...', 1)
		return answer

	#  User asking cycle !!! CALL FIRST !!!
	def ask_user(self):
		choice = self.user_menu()
		if choice == 1:
			self.analyze()
		elif choice == 2:
			self.decrease_weight()
		elif choice == 3:
			self.identify()
		else:
			raise ValueError('Illegal value "%s" recieved!' % (choice))


x = ClickbaitIdentifierUI('xd')
x.ask_user()