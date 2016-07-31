from database_tools import DatabaseTools
from word_tools # Will do later
from sentence_tools # Will do later
from logic_tools # Will do later
from utils import *


init_save_dir()


class ClickbaitIdentifierUI("""NOT REALLY SURE WHAT TO PUT HERE"""):
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
