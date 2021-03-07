import numpy as np
import pandas as pd

def pass_process(passes, exceptions)

    char_count = 0
    plays = len(passes)
    for i in range(0,plays):
        char_curr = passes[i]
        if(char_curr in exceptions):
            char_count = char_count + 1
        else:
            char_count = char_count
    
    plays_array = np.array(char_count)
    
    for i in range(0,plays)
        j = 0
        while(passes[i] not in exceptions):
            
