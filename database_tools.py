import sqlite3
from glob import glob

class DatabaseTools:
	#  Words - All together, Sentences - All together, Statistics - clickbait only
	database = {'words':{},'sentences':{},
		    'statistics':{'avg_lower':0, 'avg_start_upper':0, 
		    'avg_upper':0, 'avg_num':0}}

	def __database_exists(self):
		return glob(self.save_dir)

	def db_connect(function):
		def wrapper(self):
			if self.__database_exists():
				self.db_conn = sqlite3.connect(self.save_dir)
				self.db_cursor = self.db_conn.cursor()
				function(self)
				self.db_conn.close()
			else:
				function(self)
		return wrapper

	@db_connect
	def load_db(self):
		if self.__database_exists():
			self.db_cursor.execute("SELECT word, clickbait_index FROM Words")
			for word, clickbait_index in self.db_cursor.fetchall():
				DatabaseTools.database['words'][word] = clickbait_index

			self.db_cursor.execute("SELECT sentence, clickbait_status FROM Sentences")
			for sentence, clickbait_status in self.db_cursor.fetchall():
				clickbait_status = True if clickbait_status == 1 else False  #  Int to bool
				DatabaseTools.database['sentences'][sentence] = clickbait_status

			self.db_cursor.execute("SELECT keyword, value FROM Statistics")
			for key, value in self.db_cursor.fetchall():
				DatabaseTools.database['statistics'][key] = value
		self.db_legacy = DatabaseTools.database  #  To compare what words to delete

	#  Direct insertion of new 'profiles', no further steps needed
	def sql_insert(self, table, val1, val2):
		command = "INSERT INTO {TABLE}"\
				  " VALUES( '{val1}', {val2})".format(TABLE=table, val1=val1, val2=val2)
		self.db_cursor.execute(command)
		self.db_conn.commit()


	def sql_update(self, table, column_to_update, comparison_column, new_value, current_row):
		template = "UPDATE {TABLE} SET {VALUE} = {NEW_VALUE} WHERE {KEY} ="\
				   "{CURRENT_ROW}".format(TALBE=table, VALUE=column_to_update,
							  NEW_VALUE=new_value, KEY=comparison_column,
							  CURRENT_ROW=current_row)
		self.db_cursor.execute(command)
		self.db_conn.commit()


	def update_all(self, tables_info):  #  Ugly method, needs refactoring...
		self.remove_queue(tables_info)
		for table, values in tables_info.items():
			column = values[0]
			update_column = values[1]

			for current_row_name, new_value in DatabaseTools.database[table.lower()].items():
				if self.item_exists(table, column, current_row_name):
					if not self.is_value_current(table, update_column, column, new_value, current_row_name):
						self.sql_update(table, update_column, column, new_value, current_row_name)  #  Update
				else:
					self.sql_insert(table, current_row_name, new_value)  #  Insert

	def item_exists(self, table, column, column_value):  #  Works fine
		command = 'SELECT {COLUMN} FROM'\
		' {TABLE} WHERE {COLUMN} = ?'.format(COLUMN=column,
											 TABLE=table)
		self.db_cursor.execute(command, (column_value,))
		return len(self.db_cursor.fetchall()) > 0

	def remove_queue(self, tables_info):  #  Have to config this not sure what is wrong here....
		for table, values in self.db_legacy.items():
			for item_name, value in values.items():
				if not item_name in DatabaseTools.database[table]:
					self.item_remove(table, tables_info[table.title()][0], item_name)

	def item_remove(self, table, column, item_name):  #  Remove non-existent values
		command = 'DELETE FROM {TABLE} WHERE' \
		' {COLUMN} = "{ITEM_NAME}"'.format(TABLE=table, 
										 COLUMN=column,
										 ITEM_NAME=item_name)

		self.db_cursor.execute(command)
		self.db_conn.commit()

	def is_value_current(self, table, column_to_update, comparison_column, new_value, current_row_name):
		command = 'SELECT {COMPARISON_COLUMN} FROM {TABLE} '\
			  'WHERE {COLUMN_TO_UPDATE} = {NEW_VALUE} AND'\
			  ' {COMPARISON_COLUMN} = "{CURRENT_ROW_NAME}"'.format(COMPARISON_COLUMN=comparison_column,
									       TABLE=table, COLUMN_TO_UPDATE=column_to_update,
									       NEW_VALUE=new_value, CURRENT_ROW_NAME=current_row_name)
		self.db_cursor.execute(command)
		return len(self.db_cursor.fetchall()) > 0

	def sql_create_tables(self, tables):
		for table in tables:
			self.db_cursor.execute("CREATE TABLE IF NOT EXISTS %s" % (table))

	def save_database(self):
		self.db_conn = sqlite3.connect(self.save_dir)
		self.db_cursor = self.db_conn.cursor()
		#  ( Table_name, comparison_column, new_value )

		tables_info = {'Words':('word', 'clickbait_index'),
				       'Sentences':('sentence', 'clickbait_status'),
				       'Statistics':('keyword', 'value')}

		#  Table creation template
		tables = list(['%s(%s TEXT, %s INTEGER)' % (key, value[0], value[1]) for key, value in tables_info.items()])

		self.sql_create_tables(tables)
		self.update_all(tables_info)
