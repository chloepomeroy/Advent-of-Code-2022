#!/usr/bin/env python
# coding: utf-8

# In[4]:


text_file = open("day6.txt", "r")
packet = text_file.read()


# In[24]:


for i in range(3, len(packet)):
    ls = [packet[i-x] for x in range(0, 4)]
    if len(set(ls))==4:
        result=i+1
        break
print(f"part 1 answer: {result}")


# In[25]:


for i in range(13, len(packet)):
    ls = [packet[i-x] for x in range(0, 14)]
    if len(set(ls))==14:
        result2=i+1
        break
print(f"part 1 answer: {result2}")


# In[ ]:




