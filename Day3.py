#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

rucksacks = pd.read_csv("day3.txt", header=None, names=["items"])


# In[6]:


rucksacks["compartment 1"] = [i[:len(i)//2] for i in rucksacks["items"]]
rucksacks["compartment 2"] = [i[len(i)//2:] for i in rucksacks["items"]]


# In[27]:


packed_wrong=[]
for i in range(rucksacks.shape[0]):
    packed_wrong.append(list(set(rucksacks["compartment 1"][i]).intersection(rucksacks["compartment 2"][i]))[0])
    


# In[31]:


upper = [ord(c) for c in packed_wrong if c.isupper()]
lower = [ord(c) for c in packed_wrong if c.islower()]


# In[32]:


priority_sum = sum(upper)-38*len(upper)+sum(lower)-96*len(lower)


# In[33]:


print(f"part 1 answer: {priority_sum}")


# In[44]:


badge_types = []
for i in range(0,rucksacks.shape[0], 3):
    badge_types.append(list(set(set(rucksacks["items"][i]).intersection(rucksacks["items"][i+1])).intersection(rucksacks["items"][i+2]))[0])


# In[45]:


badge_upper = [ord(c) for c in badge_types if c.isupper()]
badge_lower = [ord(c) for c in badge_types if c.islower()]


# In[46]:


badge_sum = sum(badge_upper)-38*len(badge_upper)+sum(badge_lower)-96*len(badge_lower)


# In[47]:


print(f"part 1 answer: {badge_sum}")


# In[ ]:




