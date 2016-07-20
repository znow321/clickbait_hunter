from os import system
from time import sleep
import platform


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