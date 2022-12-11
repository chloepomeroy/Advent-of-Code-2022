#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
sections = pd.read_csv("day4.txt", sep=",", header=None, names=["Elf 1", "Elf 2"])


# In[30]:


overlap_fully_count = 0
for i in range(sections.shape[0]):
    elf1 = sections["Elf 1"][i].split("-")
    elf2 = sections["Elf 2"][i].split("-")
    
    set1 = set(range(int(elf1[0]), int(elf1[1])+1))
    set2 = set(range(int(elf2[0]), int(elf2[1])+1))
    
    if set1.issubset(set2) or set2.issubset(set1):
        overlap_fully_count += 1


# In[31]:


print(f"part 1 answer: {overlap_fully_count}")


# In[34]:


overlap_count = 0
for i in range(sections.shape[0]):
    elf1 = sections["Elf 1"][i].split("-")
    elf2 = sections["Elf 2"][i].split("-")
    
    set1 = set(range(int(elf1[0]), int(elf1[1])+1))
    set2 = set(range(int(elf2[0]), int(elf2[1])+1))
    
    if len(set1.intersection(set2))!=0:
        overlap_count += 1


# In[33]:


print(f"part 2 answer: {overlap_count}")


# In[ ]:




