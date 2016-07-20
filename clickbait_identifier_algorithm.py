from re import findall
from os import path
from statistics import mean  #  Will be implemented later
from database_tools import DatabaseTools
from word_tools import WordTools
from sentence_tools import SentenceTools
import make_save_dir
from utils import *


init_save_dir.init()


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
		self.save_dir = path.join('clickbait_database', 'database.sqlite')

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
x.load_db()
DatabaseTools.database = {'words':{'My first word':15},'sentences':{'This is a new test sentence':0},
			  'statistics':{'avg_lower':12, 'avg_start_upper':5, 
			  'avg_upper':15, 'avg_num':10}}
x.user_menu()
x.save_database()
