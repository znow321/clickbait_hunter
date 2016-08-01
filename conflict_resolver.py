def resolve_conflicts(clickbait_status):  #  = conflicting status
    choice = get_answer(clickbait_status)
	if choice == 'y':
		return not clickbait_status
	elif choice == 'n':
		return clickbait_status


def get_answer(clickbait_status): # Asking cycle
	while True:
		try:
			choice = input(get_question())
			assert(choice.lower() in ['y', 'n'])
			return choice
		except (ValueError, AssertionError):
			error('Invalid option entered, please try again...', 1)


def get_question(clickbait_status):
    sentence = database.sentence
	status = ('clickbait', 'non-clickbait')
	if clickbait_status: 
		status = status[::-1]
	sentence = 'Do you wan\'t to toggle the "%s" sentence status' \
			'from %s to %s?\n(Y/N)' % (sentence, status[0], status[1])
	return sentence
