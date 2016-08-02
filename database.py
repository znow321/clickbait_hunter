class database: # Universal data storage function
    sentence = ''
    clb_status = False
    tables = ('Words', 'Sentences', 'Statistics', 'Stat_aux')
    database = {'Words':{},'Sentences':{},
                'Statistics':{'avg_lower':0, 
                'avg_start_upper':0, 
                'avg_upper':0, 'avg_int':0},
                'Stat_aux':{'num_lower':0,
                'num_start_upper':0,
                'num_upper':0,
                'num_int':0}}
    db_legacy = {}  #  Original copy for db item removal
