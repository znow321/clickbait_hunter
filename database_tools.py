import sqlite3
from utils import get_save_dir, database_exists


class database:
    tables = ('Words', 'Sentences', 'Statistics')

    database = {'Words':{},'Sentences':{},
                'Statistics':{'avg_lower':0, 
                'avg_start_upper':0, 
                'avg_upper':0, 'avg_num':0}}

    db_legacy = {}  #  Original copy for db item removal


def db_connect():
    database.db_conn = sqlite3.connect(get_save_dir())
    database.db_cursor = database.db_conn.cursor()


def db_disconnect():
    database.db_conn.close() 


def db_execute(command):
    database.db_cursor.execute(command)
    database.db_conn.commit()


def db_fetch():
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


def remove_queue():  
    for table, values in database.db_legacy.items():
        for item, value in values.items():
            if not item in database.database[table]:
                sql_remove(table, item)


def db_save(): # INTERFACE FUNCTION
    db_connect()
    sql_create_tables()
    update_all()
    db_disconnect()


def db_load():
    if database_exists():
        db_connect()
        for table in database.tables: 
            db_execute("SELECT item, value FROM %s" % (table))                                   
            for item, value in db_fetch():
                database.database[table][item] = value
        db_disconnect()
    database.db_legacy = database.database


def gen_tables():
    #  Table creation template
    for table in database.tables:
        yield '%s(item TEXT, value INTEGER)' % (table)


def sql_create_tables():
    tables = list(gen_tables())
    for table in tables:
        db_execute("CREATE TABLE IF NOT EXISTS %s" % (table))


#  Direct insertion of new 'profiles', no further steps needed
def sql_insert(table, item, value):
    command = "INSERT INTO {table}"\
              " VALUES( '{item}', {value})".format(table=table, 
                                                   item=item, 
                                                   value=value)
    db_execute(command)


def sql_update(table, item , value):
    command = 'UPDATE {table} SET value = {value} WHERE item ='\
               ' "{item}"'.format(table=table, value=value, item=item)
    db_execute(command)


def sql_remove(table, item):  #  Remove non-existent values
    command = 'DELETE FROM {table} WHERE' \
            ' item = "{item}"'.format(table=table,item=item)
    db_execute(command)


def is_value_current(table, item, value):
    command = 'SELECT item FROM {table} '\
              'WHERE value = {value} AND '\
              'item = "{item}"'.format(table=table, item=item, value=value)
    db_execute(command)
    return len(db_fetch()) > 0


def item_exists(table, item):  #  Works fine
    command = 'SELECT item FROM'\
                ' {table} WHERE item = "{item}"'.format(table=table, item=item)
    db_execute(command)
    return len(db_fetch()) > 0
