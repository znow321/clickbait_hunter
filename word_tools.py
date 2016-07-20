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


