def increase_weight(sentence):
	for word in sentence:
		if in_database(word):
			DatabaseTools.database['words'][word] += 1
		else:
			DatabaseTools.database['words'][word] = 1


def decrease_weight(sentence):
	for word in sentence:
		if decrease_check(word):
			DatabaseTools.database['words'][word] -= 1


def decrease_check(word):
	return in_database(word) and can_subtract(word)


def in_database(word):
	return word in DatabaseTools.database['words']


def can_substract(word):
	return DatabaseTools.database['words'][word] >= 1
