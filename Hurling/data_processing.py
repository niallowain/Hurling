import numpy as np

def pass_process(passes, exceptions):

    char_count = 0
    plays = len(passes)
    for i in range(0,plays):
        char_curr = passes[i]
        if(char_curr in exceptions):
            char_count = char_count + 1
        else:
            char_count = char_count
    
    plays_array = np.zeros((plays,plays))
    j = k = 0
    count = 0
    for i in range(0,plays):
        if(passes[i] not in exceptions):
            plays_array[j,k] = passes[i]
            i = i+1
            k = k+1
            if(k>count):
                count = k
        else:
            i = i+1
            j = j + 1
            k = 0
            
    
    return plays_array[0:j,0:count]
