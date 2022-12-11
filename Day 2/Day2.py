#!/usr/bin/env python
# coding: utf-8

# In[37]:


import pandas as pd
inputs = pd.read_csv("day2.csv", sep=" ", header=None, names=["Opponent Move", "Suggested Move"])


# In[38]:


Rock_count = inputs[inputs["Suggested Move"]=="X"].shape[0]
Paper_count = inputs[inputs["Suggested Move"]=="Y"].shape[0]
Scissor_count = inputs[inputs["Suggested Move"]=="Z"].shape[0]


# In[39]:


total_points = Rock_count*1+Paper_count*2+Scissor_count*3

def get_outcome(x, y):
    if (x=="A" and y=="X") or (x=="B" and y=="Y") or (x=="C" and y=="Z"):
        return 3
    elif (x=="A" and y=="Y") or (x=="B" and y=="Z") or (x=="C" and y=="X"):
        return 6
    else:
        return 0

for i in range(inputs.shape[0]):
    total_points += get_outcome(inputs["Opponent Move"][i], inputs["Suggested Move"][i])


# In[40]:


print(f"part 1 answer: {total_points}")


# In[41]:


Lose_count = inputs[inputs["Suggested Move"]=="X"].shape[0]
Draw_count = inputs[inputs["Suggested Move"]=="Y"].shape[0]
Win_count = inputs[inputs["Suggested Move"]=="Z"].shape[0]


# In[42]:


total_points2 = Lose_count*0+Draw_count*3+Win_count*6


# In[43]:


def get_move(x, y):
    if (x=="A" and y=="X") or (x=="B" and y=="Z") or (x=="C" and y=="Y"):
        return 3
    elif (x=="A" and y=="Z") or (x=="B" and y=="Y") or (x=="C" and y=="X"):
        return 2
    else:
        return 1

for i in range(inputs.shape[0]):
    total_points2 += get_move(inputs["Opponent Move"][i], inputs["Suggested Move"][i])


# In[44]:


print(f"part 2 answer: {total_points2}")

