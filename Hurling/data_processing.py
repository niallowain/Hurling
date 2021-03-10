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

def adj_mat(plays_array):
    init_mat = np.zeros((16,16))
    for i in range(0,int(plays_array.shape[0])-1):
        for j in range(0,int(plays_array.shape[1])-1):
            pass_val = [int(plays_array[i,j]),int(plays_array[i,j+1])]
            if(pass_val[0] == 0):
                init_mat[i,j] = init_mat[i,j] 
            else : 
                row_val = int(pass_val[0] )
                col_val = int(pass_val[1] )
                init_mat[row_val,col_val] = int(init_mat[row_val,col_val]) + 1

    return init_mat[1:15,1:15]

def weight_out(adj_mat):
    weight_vec = np.zeros(15)
    for i in range(0,15):
            weight_vec[i] = sum(adj_mat[i,])/sum(sum(adj_mat[0:14,]))
            
    return weight_vec
                       
