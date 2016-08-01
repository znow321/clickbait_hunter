from re import findall
from statistics import mean  #  Will be implemented later


def identify(self):  # If sentence if flagged as clickbait. INTERFACE FUNCTION
	pass


def report_gen():
    sentence = database.sentence
	yield sentence.split()
	yield findall(r'\b[a-z\']+\b', sentence)
	yield findall(r'\b[A-Z][a-z\']+\b', sentence)
	yield findall(r'\b[A-Z\']+\b', sentence)
	yield findall(r'\b[0-9]+\b', sentence)


def report_enum():
    sentence = database.sentence
	stats = list(report_gen(sentence))
	return [len(word_type) for word_type in stats]


def percentages():
    sentence = database.sentence
	report = report_enum(sentence)
	percent_per_word = 100 / report[0]
	for word_type in report[1:]:
		yield word_type * percent_per_word
