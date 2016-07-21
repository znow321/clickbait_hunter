from re import findall


class LogicTools:
	#  If the sentence is flagged as clickbait
	def identify(self):
		pass


def report_gen(sentence):
	yield sentence.split()
	yield findall(r'\b[a-z\']+\b', sentence)
	yield findall(r'\b[A-Z][a-z\']+\b', sentence)
	yield findall(r'\b[A-Z\']+\b', sentence)
	yield findall(r'\b[0-9]+\b', sentence)


def report_enum(sentence):
	stats = list(report_gen(sentence))
	return [len(word_type) for word_type in stats]


def percentages(sentence):
	report = report_enum(sentence)
	percent_per_word = 100 / report[0]
	for word_type in report[1:]:
		yield word_type * percent_per_word