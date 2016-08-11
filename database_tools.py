from utils import db_exists, get_save_dir, sentence_db, word_db
import sqlite3
from utils import db


db_disconnect = lambda: db.db_conn.close() 


db_fetch = lambda: db.db_cursor.fetchall()


def db_connect():
    db.db_conn = sqlite3.connect(get_save_dir())
    db.db_cursor = db.db_conn.cursor()


def db_execute(command):
    db.db_cursor.execute(command)
    db.db_conn.commit()


def remove_queue():  
    for table, values in db.db_legacy.items():
        for item, value in values.items():
            if not item in db.database[table]:
                sql_remove(table, item)


def db_save(): # INTERFACE FUNCTION
    db_connect()
    sql_create_tables()
    remove_queue()
    bool_convertor("bool_to_binary")
    for table in db.tables:
            for item, value in db.database[table].items():
                if item_exists(table, item):
                    if not is_value_current(table, item, value): 
                        sql_update(table, item, value)
                else:
                    sql_insert(table, item, value )
    db_disconnect()


def db_load(): # SECOND INTERFACE FUNCTION
    if database_exists():
        db_connect()
        for table in db.tables: 
            db_execute("SELECT item, value FROM %s" % (table))                                   
            for item, value in db_fetch():
                db.database[table][item] = value
        bool_convertor("binary_to_bool")
        db_disconnect()
    database.db_legacy = db.database


def bool_convertor(mode):
    if mode == "bool_to_binary":
        for key, value in sentence_db.items(): 
            if value == True:
                db.database['sentences'][key] = 1
            else:
                db.database['sentences'][key] = 0
    elif mode == "binary_to_bool":
        for key, value in sentence_db().items(): 
            if value == 1:
                db.database['sentences'][key] = True
            elif value == 0:
                db.database['sentences'][key] = False


def gen_tables():
    #  Table creation template
    for table in db.tables:
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
