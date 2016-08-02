def analyze():  # AFTER IDENTIFYING
    wordcount = report_len() 
    stat_names = None # Will do later

    for value, item in zip(wordcount, stat_names): # Word counts are all I need 
        database['Statistics'][item] += value 
   
    update_sentence_db() 
