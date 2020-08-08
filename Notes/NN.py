#%%
####
# And function example 
####

import numpy as np
bias = -30
w1 = 20
w2 = 20
x = np.array([[0,1,0,1], [0,0,1,1]] )

row,col = x.shape
result = []
result_ =[]
for i in range(col):
    x1 = x[0][i]
    x2 = x[1][i]
    result.append(g(x1,x2,bias,w1,w2))
    result_.append(1 - result[i])

print(result)
print(result_)

def g(x1,x2,bias,w1,w2):
    result = bias + w1 * x2 + w2 * x2 
    result =  1/(1 + np.exp(-result))
    return result




# %%
