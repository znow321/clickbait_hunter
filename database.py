class database: # Universal data storage function
    sentence = ''
    clb_status = False
    tables = ('Words', 'Sentences', 'Statistics')

    database = {'Words':{},'Sentences':{},
                'Statistics':{'num_lower':0, # Total number of analyzed specimens needed for statistical analysis
                'num_start_upper':0,
                'num_upper':0,
                'num_int':0}}

    db_legacy = {}  #  Original copy for db item removal
