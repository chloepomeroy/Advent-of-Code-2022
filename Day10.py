#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

np.set_printoptions(threshold=np.inf)
np.set_printoptions(linewidth=np.inf)


# In[1]:


text_file = open("day10.txt", "r")
data = text_file.read()
commands= data.split('\n')


# In[52]:


def get_signal_strengths(commands): 
    cycle = 1
    X = 1
    signal_strengths = []
    strength_sum = 0

    for command in commands:
        if command=='noop':
            signal_strengths.append(cycle*X)
            cycle += 1
        else:
            signal_strengths.append(cycle*X)
            cycle += 1
            signal_strengths.append(cycle*X)
            cycle += 1

            X += float(command.split()[1])      
    for i in [19, 59, 99, 139, 179, 219]:
        strength_sum += signal_strengths[i]
        
    return strength_sum


# In[54]:


print(f"part 1 answer: {get_signal_strengths(commands)}")


# In[91]:


def get_message(commands):
    cycle = 1
    X = 1
    x_cycle = []
    drawing = []
    
    for command in commands:
        if command=='noop':
            x_cycle.append((cycle-1, X))
            cycle += 1
        else:
            x_cycle.append((cycle-1, X))
            cycle += 1
            x_cycle.append((cycle-1, X))
            cycle += 1

            X += float(command.split()[1])
    
    for val in x_cycle:
        if int(val[0])%40 in [int(val[1])-1, int(val[1]), int(val[1])+1]:
            drawing.append("#")
        else:
            drawing.append(".")
    final_message = np.array([drawing[0:40], drawing[40:80], drawing[80:120], drawing[120:160], drawing[160:200], drawing[200:240]])

    return final_message


# In[93]:


print("part 2 answer:")
print(draw_image(commands))


# In[ ]:




