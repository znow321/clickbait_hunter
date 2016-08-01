from conflict_resolver import resolve_conflicts


def update_sentence_database(clickbait_status=True):
    sentence = database.sentence
	if not can_automerge():
		clickbait_status = resolve_conflicts(clickbait_status)
		database.database['Sentences'][sentence] = clickbait_status
    

def in_database(clickbait_status):
    sentence = database.sentence
	return sentence in database.database['Sentences']


def in_conflict(clickbait_status):
    sentence = database.sentence
	return database.database['Sentences'][sentence] != clickbait_status


def can_automerge(clickbait_status):
    sentence = database.sentence
	in_database = in_database(sentence, clickbait_status)
	in_conflict = in_conflict(sentence, clickbait_status)
	return in_database and not in conflict


resolve_conflicts(False)
