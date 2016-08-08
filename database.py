class database: # Universal data storage function
    sentence = ''
    clb_status = None
    tables = ('words', 'sentences')
    database = {'words':{},'sentences':{}}
    db_legacy = {}  #  Original copy for db item removal
