#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
l=[2,3]
for i in range(5,101):
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            break
    else:
        l.append(i)
print(" ".join(map(str,l)))


# In[ ]:




