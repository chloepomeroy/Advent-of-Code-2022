#!/usr/bin/env python
# coding: utf-8

# In[30]:


import pandas as pd


# In[32]:


moves = pd.read_csv("input.txt", header=None, names=["moves"])


# In[33]:


moves["Number of crates"] = moves["moves"].str.extract('(\d+)')
moves["From"] = moves["moves"].str.extract('\d.*(\d+).*\d')
moves["To"] = moves["moves"].str.extract('\d.*(\d+)')


# In[42]:


positions = ['NDMQBPZ', 'CLZQMDHV', 'QHRDVFZG', 'HGDFN', 'NFQ', 'DQVZFBT', 'QMTZDVSH', 'MGFPNQ', 'BWRM']

for i in range(moves.shape[0]):
    fr = int(moves["From"][i])-1
    to = int(moves["To"][i])-1
    for j in range(int(moves["Number of crates"][i])):
        positions[fr], positions[to] = positions[fr][:-1], positions[to]+positions[fr][-1]

print(f"part 1 answer: {''.join([c[-1] for c in positions])}")


# In[54]:


positions2 = ['NDMQBPZ', 'CLZQMDHV', 'QHRDVFZG', 'HGDFN', 'NFQ', 'DQVZFBT', 'QMTZDVSH', 'MGFPNQ', 'BWRM']

for i in range(moves.shape[0]):
    fr = int(moves["From"][i])-1
    to = int(moves["To"][i])-1
    num = int(moves["Number of crates"][i])
    positions2[fr], positions2[to] = positions2[fr][:-num], positions2[to]+positions2[fr][-num:]

print(f"part 2 answer: {''.join([c[-1] for c in positions2])}")


# In[ ]:




