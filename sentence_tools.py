def update_sentence_database(sentence, clickbait_status=True):
	if not can_automerge():
		clickbait_status = resolve_conflicts(clickbait_status)
		DatabaseTools.database['sentences'][sentence] = clickbait_status


def in_database(sentence, clickbait_status):
	return sentence in DatabaseTools.database['sentences']


def in_conflict(sentence, clickbait_status):
	return DatabaseTools.database['sentences'][sentence] != clickbait_status


def can_automerge(sentence, clickbait_status):
	in_database = in_database(sentence, clickbait_status)
	in_conflict = in_conflict(sentence, clickbait_status)
	return in_database and not in conflict


def resolve_conflicts(clickbait_status):  #  = conflicting status
	if choice == 'y':
		return not clickbait_status
	else:
		return clickbait_status


def get_answer(clickbait_status):
	while True:
		try:
			choice = input(get_question())
			assert(choice.lower() in ['y', 'n'])
			return choice
		except (ValueError, AssertionError):
			error('Invalid option entered, please try again...', 1)


def get_question(clickbait_status):
	status = ('clickbait', 'non-clickbait')
	if clickbait_status: 
		status = status[::-1]
	sentence = 'Do you wan\'t to toggle the "%s" sentence status' \
			'from %s to %s?\n(Y/N)' % (sentence, status[0], status[1])
	return sentence
