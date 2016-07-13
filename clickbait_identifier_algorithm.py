from re import findall, sub
import sqlite3
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
	#  Moving to sql
	database = {'words':{},'sentences':{},
				'statistics':{'avg_lower':0, 'avg_start_upper':0, 
				'avg_upper':0, 'avg_num':0}}
	
	def __database_exists(self):
		return glob(self.save_dir)
	
	def load_database(self):
		if self.__database_exists():

			self.db_cursor.execute("SELECT word, clickbait_index FROM Words")
			for word, clickbait_index in db_load_cursor.fetchall():
				DatabaseTools.database['words'][word] = clickbait_index

			self.db_cursor.execute("SELECT sentence, clickbait_status FROM Sentences")
			for sentence, clickbait_status in db_load_cursor.fetchall():
				clickbait_status = True if clickbait_status == 1 else False  #  Int to bool
				DatabaseTools.database['sentences'][sentence] = clickbait_status

			self.db_cursor.execute("SELECT keyword, value FROM Statistics")
			for key, value in db_load_cursor.fetchall():
				DatabaseTools.database['statistics'][key] = value
	
	def sql_insert(self, table, key, value):
		template = "INSERT INTO {TABLE} VALUES( ?, ?)"
		command = sub('{TABLE}', table.title(), template)
		self.db_cursor.execute(command, (key, value))

	def sql_update(self, table, column_to_update, keyword, value):
		template = "UPDATE {TABLE} SET {VALUE} = ?" \
						   " WHERE {KEY}='{KEY}'"
		command = sub('{TABLE}', table, template)
		command = sub('{VALUE}', column_to_update, command)
		command = sub('{KEY}', keyword, command)
		self.db_cursor.execute(command, (value))
						   # {VALUE} = Clickbait index etc., {KEY} = Word or sentence name

	def is_value_current(self, table, column, key, value, new_value):
		pass


	def sql_create_tables(self, tables):
		for table in tables:
			self.db_cursor.execute("CREATE TABLE IF NOT EXISTS %s" % (table))

	def save_database(self):
		self.db_conn = sqlite3.connect(self.save_dir)
		self.db_cursor = self.db_save_conn.cursor()

		tables = ('Words(word TEXT, clickbait_index INTEGER)', 
				  'Sentences(sentence TEXT, clickbait_status INTEGER)',  #No native support for bools..
				  'Statistics(keyword TEXT, value INTEGER)')

		for table, columns in DatabaseTools.database.items():
			command = sub("{TABLE}", table.title(), command_base)
			for key, value in DatabaseTools.database[table].items():
				if not self.__database_exists():
					pass
				self.db_cursor.execute(command, (key, value))

		self.db_conn.commit()


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
		while True:
			try:
				choice = input(say)
				assert(choice.lower() in ['y', 'n'])
				break
			except ValueError, AssertionError:
				error('Invalid option entered, please try again...', 1)
		if choice = 'y':
			return not clickbait_status
		else:
			return clickbait_status


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
		self.save_dir = 'clickbait_database\\database.db'
		self.load_database()
		self.db_conn = sqlite3.connect(self.save_dir)
		self.db_cursor = self.db_conn.cursor()
		

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
DatabaseTools.database = {'words':{'Testing sql':1999, 'SQLite':42}, 
						  'sentences':{'Kazooo kid':True, 'Haxors are cool':True}, 
						  'statistics':{'avg_lower':42, 'avg_start_upper':1337, 'avg_upper':404, 'avg_num':1}}
x.save_database()