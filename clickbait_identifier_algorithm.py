from re import findall, sub
import sqlite3
from os import system, path, makedirs
from time import sleep
from glob import glob
from statistics import mean
import platform


def cls():
	if platform.system() == 'Linux':
		system('clear')
	elif platform.system() == 'Windows':
		system('cls')
	else:
		raise Exception('Shutting down, unknown operating system detected...')


#  Creates save directory with a .gitignore if it's not already there
if not path.exists('clickbait_database'):  
	makedirs('clickbait_database')
	create_gitignore = open(join('clickbait_database','.gitignore'), 'w')
	create_gitignore.write('*\n!.gitignore')
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


	def __database_exists(self):
		return glob(self.save_dir)
	
	def db_connect(function):
		def wrapper(self):
			if self.__database_exists():
				self.db_conn = sqlite3.connect(self.save_dir)
				self.db_cursor = self.db_conn.cursor()
				function(self)
				self.db_conn.close()
			else:
				function(self)
		return wrapper

	@db_connect
	def load_database(self):
		if self.__database_exists():
			self.db_connect()
		self.db_copy = DatabaseTools.database  #  To compare what words to delete
		if self.__database_exists():
			self.db_cursor.execute("SELECT word, clickbait_index FROM Words")
			for word, clickbait_index in self.db_cursor.fetchall():
				DatabaseTools.database['words'][word] = clickbait_index

			self.db_cursor.execute("SELECT sentence, clickbait_status FROM Sentences")
			for sentence, clickbait_status in self.db_cursor.fetchall():
				clickbait_status = True if clickbait_status == 1 else False  #  Int to bool
				DatabaseTools.database['sentences'][sentence] = clickbait_status

			self.db_cursor.execute("SELECT keyword, value FROM Statistics")
			for key, value in self.db_cursor.fetchall():
				DatabaseTools.database['statistics'][key] = value
	
	#  Direct insertion of new 'profiles', no further steps needed
	def sql_insert_command(self, table):  
		template = "INSERT INTO {TABLE} VALUES( ?, ?)"
		return sub('{TABLE}', table, template)

	def sql_update_command(self, table, column_to_update, comparison_column):
		template = "UPDATE {TABLE} SET {VALUE} = (?) WHERE {KEY}= (?) "
		command = sub('{TABLE}', table, template)
		command = sub('{VALUE}', column_to_update, command)
		return sub('{KEY}', comparison_column, command)

	def sql_update_or_input(self, tables_info):
		self.remove_queue()  # DEBUG
		for table in tables_info:
			for current_row_name, new_value in DatabaseTools.database[table[0].lower()].items():
				if self.item_exists(table[0], table[1], current_row_name):
					if not self.is_value_current(table[0], table[2], table[1], new_value, current_row_name):
						command = self.sql_update_command(table[0], table[2], table[1])
						print(command)
						self.db_cursor.execute(command, (new_value, current_row_name))  #  Update
				else:
					command = self.sql_insert_command(table[0])
					self.db_cursor.execute(command, (current_row_name, new_value))  #  Insert

	def item_exists(self, table, column, column_value):
		template = 'SELECT {COLUMN} FROM {TABLE} WHERE {COLUMN} = ?'
		command = sub('{COLUMN}', column, template)
		command = sub('{TABLE}', table, command)
		self.db_cursor.execute(command, (column_value,))
		return len(self.db_cursor.fetchall()) > 0

	def remove_queue(self): 
		for current, legacy in zip(DatabaseTools.database, self.db_copy):
			print(current)
			input(legacy)

	def item_remove_command(self, table, column):  #  Remove non-existent values
		template = 'DELETE FROM {TABLE} WHERE {COLUMN} = ?'
		command = sub('{TABLE}', table, template)
		return sub('{COLUMN}', column, command)

	def is_value_current(self, table, column_to_update, comparison_column, new_value, current_row_name):
		template = 'SELECT {COMPARISON_COLUMN} FROM {TABLE} WHERE {COLUMN_TO_UPDATE} = ? AND {COMPARISON_COLUMN} = ?'
		command = sub('{COMPARISON_COLUMN}', comparison_column, template)
		command = sub('{TABLE}', table, command)
		command = sub('{COLUMN_TO_UPDATE}', column_to_update, command)
		self.db_cursor.execute(command, (new_value, current_row_name))
		return len(self.db_cursor.fetchall()) > 0

	def sql_create_tables(self, tables):
		for table in tables:
			self.db_cursor.execute("CREATE TABLE IF NOT EXISTS %s" % (table))

	def save_database(self):
		self.db_conn = sqlite3.connect(self.save_dir)
		self.db_cursor = self.db_conn.cursor()
		#  ( Table_name, comparison_column, new_value )
		tables_info = (('Words', 'word', 'clickbait_index'),
				       ('Sentences', 'sentence', 'clickbait_status'),
				       ('Statistics', 'keyword', 'value'))

		#  Table creation template
		tables = list(['%s(%s TEXT, %s INTEGER)' % (table, key, value) for table, key, value in tables_info])
		
		self.sql_create_tables(tables)
		self.sql_update_or_input(tables_info)
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
			except (ValueError, AssertionError):
				error('Invalid option entered, please try again...', 1)
		if choice == 'y':
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
		self.save_dir = path.join('clickbait_database', 'database.db')

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
x.save_database()