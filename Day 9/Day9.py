#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


steps = pd.read_csv("input.csv", header=None, names=["steps"])
steps['Direction'] = steps["steps"].str[0]
steps['Number'] = steps["steps"].str.extract('(\d+)')


# In[20]:


def sign_function(x): 
        if x > 0: 
            return 1 
        elif x == 0: 
            return 0
        else:
            return -1

def get_unique_tail_positions(data):
    h_posns = [(0,0)]
    t_posns = [(0,0)]
    h_y = 0
    h_x = 0
    sumposn = 0    

    for i in range(data.shape[0]):
        for j in range(int(data.Number[i])):
            if data.Direction[i]=="U":
                h_y += 1
            if data.Direction[i]=="D":
                h_y -= 1
            if data.Direction[i]=="R":
                h_x += 1
            if data.Direction[i]=="L":
                h_x -= 1
            h_posns.append((h_x, h_y))        
            x_diff = h_x-t_posns[sumposn][0]
            y_diff = h_y-t_posns[sumposn][1]
       
            if y_diff**2 < 4 and x_diff**2 < 4:
                t_x = t_posns[sumposn][0]
                t_y = t_posns[sumposn][1]
            else:
                t_x = t_posns[sumposn][0]+sign_function(x_diff)
                t_y = t_posns[sumposn][1]+sign_function(y_diff)
            t_posns.append((t_x, t_y))

            sumposn += 1
    return len(set(t_posns))


# In[21]:


print(f"part 1 answer: {get_unique_tail_positions(steps)}")


# In[45]:


def get_positions(data, n):
    h_posns = [(0,0)]
    h_y = 0
    h_x = 0   

    for i in range(data.shape[0]):
        for j in range(int(data.Number[i])):
            if data.Direction[i]=="U":
                h_y += 1
            if data.Direction[i]=="D":
                h_y -= 1
            if data.Direction[i]=="R":
                h_x += 1
            if data.Direction[i]=="L":
                h_x -= 1
            h_posns.append((h_x, h_y)) 

    for i in range(n):
        t_posns = [(0,0)]
        sumposn = 0 
        for position in h_posns:
            x_diff = position[0]-t_posns[sumposn][0]
            y_diff = position[1]-t_posns[sumposn][1]

            if y_diff**2 < 4 and x_diff**2 < 4:
                t_x = t_posns[sumposn][0]
                t_y = t_posns[sumposn][1]
            else:
                t_x = t_posns[sumposn][0]+sign_function(x_diff)
                t_y = t_posns[sumposn][1]+sign_function(y_diff)
            t_posns.append((t_x, t_y))            
            sumposn += 1
            
        h_posns = t_posns
            
    return len(set(t_posns))
    


# In[46]:


print(f"part 2 answer: {get_positions(steps, 9)}")


# In[ ]:




