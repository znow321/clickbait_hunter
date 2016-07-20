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


