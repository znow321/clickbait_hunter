import sqlite3
from glob import glob
from utils import get_save_dir, database_exists


#  Name column = "item", Value column = "value"


class database:
    tables = ('Words', 'Sentences', 'Statistics')

    database = {'Words':{},'Sentences':{},
                'Statistics':{'avg_lower':0, 
                'avg_start_upper':0, 
                'avg_upper':0, 'avg_num':0}}

    database_legacy = None  #  Original copy for db item removal

    def connect(self):
        database.db_conn = sqlite3.connect(get_save_dir())
        database.db_cursor = database.db_conn.cursor()

    def disconnect(self):
        database.db_conn.close() 

    def execute(self, command):
        database.db_cursor.execute(command)
        database.db_conn.commit()

    def fetch(self):
        return database.db_cursor.fetchall()


def update_all(tables_info):  #  Ugly method, needs refactoring...
    remove_queue()
    for table in database.tables:
        pass
        for current_row_name, new_value in database.database[table].items():
            if item_exists(table, current_row_name):
                if not 


    # MAINTENANCE -------------------------------------------------- 
	remove_queue(tables_info)
	for table, values in tables_info.items():
		column = values[0]
		update_column = values[1]
		for current_row_name, new_value in DatabaseTools.database[table.lower()].items():
			if item_exists(table, column, current_row_name):
				if not is_value_current(table, update_column, column, new_value, current_row_name):
					sql_update(table, update_column, column, new_value, current_row_name)  #  Update
			else:
				sql_insert(table, current_row_name, new_value)  #  Insert


def remove_queue():  #  Have to config this not sure what is wrong here....
	for table, values in database.db_legacy:
		for item, value in values.items():
			if not name in database.database[table]:
                    item_remove(table, item_name)


def save_database(self):
	#  ( Table_name, comparison_column, new_value )
	sql_create_tables()
	update_all(tables_info)


def gen_tables():
	#  Table creation template
    for table in database.tables:
        yield '%s(item TEXT, value INTEGER)' % (table)


def sql_create_tables():
    tables = list(gen_tables())
	for table in tables:
		database.execute("CREATE TABLE IF NOT EXISTS %s" % (table))


def load_db(tables):  #  REMAKE
	if database_exists():
        for table in database.tables: 
            database.execute("SELECT item, value FROM %s" % (table))                                   
            for item, value in database.fetch():
                database.database[table][item] = value
    database.db_legacy = database.database


#  Direct insertion of new 'profiles', no further steps needed
def sql_insert(table, item, value):
	command = "INSERT INTO {table}"\
			  " VALUES( '{item}', {value})".format(table=table, item=item, value=value)
    database.execute(command)


def sql_update(table, new_value, current_row):
	command = "UPDATE {table} SET value = {new_value} WHERE item ="\
               "{current_row}".format(talbe=table, 
                                      new_value=new_value, 
                                      current_row=current_row)
    database.execute(command)


def sql_remove(table, item_name):  #  Remove non-existent values
	command = 'DELETE FROM {TABLE} WHERE' \
              ' item = "{ITEM_NAME}"'.format(TABLE=table, 
                                             ITEM_NAME=item_name)
    database.execute(command)


def is_value_current(table, new_value, cur_row_name):
	command = 'SELECT item FROM {table} '\
		      'WHERE value = {new_value} AND'\
		      'item = "{cur_row_name}"'.format( table=table, 
                                                new_value=new_value, 
                                                cur_row_name=cur_row_name)
    database.execute(command)
	return len(database.fetch()) > 0


def item_exists(table, item):  #  Works fine
	command = 'SELECT item FROM'\
              ' {table} WHERE item = {item}'.format(table=table,
                                                    item=item)
    database.execute(command)
	return len(database.fetch()) > 0


