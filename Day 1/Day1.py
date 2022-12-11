#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[48]:


cal = open("input.txt", "r")
data = cal.read()


# In[52]:


sums=[]
for elf in data.split("\n\n"):
    sums.append(sum([int(snack_calories) for snack_calories in elf.split("\n")]))


# In[54]:


#get the highest calorie sum
print(f"part 1 answer: {max(sums)}")


# In[63]:


sums.sort(reverse=True)

# get sum of top three elves
print(f"part 2 answer: {sum(sums[0:3])}")

