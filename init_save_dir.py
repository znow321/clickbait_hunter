from os import path, makedirs


#  Creates save directory with a .gitignore if it's not already there
def init():
	if not path.exists('clickbait_database'):
		makedirs('clickbait_database')
		create_gitignore = open(join('clickbait_database','.gitignore'), 'w')
		create_gitignore.write('*\n!.gitignore')
		create_gitignore.close()