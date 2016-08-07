class database: # Universal data storage function
    sentence = ''
    clb_status = False
    tables = ('words', 'sentences')

    database = {'words':{},'sentences':{},
                'statistics':{'num_lower':0, # Total number of analyzed specimens needed for statistical analysis
                'num_upper_start':0,
                'num_upper':0,
                'num_int':0}}

    db_legacy = {}  #  Original copy for db item removal
