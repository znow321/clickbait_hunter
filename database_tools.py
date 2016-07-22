import sqlite3
from glob import glob
from utils import get_save_dir, database_exists


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


def update_all():  
    remove_queue()
    for table in database.tables:
        for item, value in database.database[table].items():
            if item_exists(table, item):
                if not is_value_current(table, item, value): 
                    sql_update(table, item, value)
            else:
                sql_insert(table, item, value )


def remove_queue():  #  Have to config this not sure what is wrong here....
	for table, values in database.db_legacy:
	    for item, value in values.items():
		    if not name in database.database[table]:
                sql_remove(table, item)


def save_database():
	#  ( Table_name, comparison_column, new_value )
    database.connect()
	sql_create_tables()
	update_all()
    database.disconnect()


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


def sql_update(table, item , value):
	command = "UPDATE {table} SET value = {value} WHERE item ="\
               "{item}".format(talbe=table, value=value, item=item)
    database.execute(command)


def sql_remove(table, item):  #  Remove non-existent values
	command = 'DELETE FROM {table} WHERE' \
              ' item = "{item}"'.format(table=table,item=item)
    database.execute(command)


def is_value_current(table, item, value):
	command = 'SELECT item FROM {table} '\
		      'WHERE value = {value} AND'\
		      'item = "{item}"'.format(table=table, item=item, value=value)
    database.execute(command)
	return len(database.fetch()) > 0


def item_exists(table, item):  #  Works fine
	command = 'SELECT item FROM'\
              ' {table} WHERE item = {item}'.format(table=table,
                                                    item=item)
    database.execute(command)
	return len(database.fetch()) > 0

database.database={'Words':{'Hello':10, 'Xd':100}, 'Sentences':{'Will it
work?':1}, 'Statistics':{'avg_lower':10, 
                         'avg_start_upper':3, 
                         'avg_upper':2, 'avg_num':9}}}

save_database()
