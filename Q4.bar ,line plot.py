#!/usr/bin/env python
# coding: utf-8

# In[17]:


import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()


# In[18]:


plt.plot([1,2,3,4],[1,4,9,16])
plt.show()


# In[19]:


plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.plot([1,2,3,4],[1,4,9,16],'r--')
plt.show()


# In[32]:


import matplotlib.pyplot as plt
import numpy as np
car=['BMW','porshe','juaguar','ford','creta','mercedes']
data=[40,34,28,18,39,50]
fig=plt.figure(figsize=(10,7))
plt.pie(data,labels=car)
plt.show()


# In[1]:


import matplotlib.pyplot as plt
import numpy as np

# Generating sample data
categories = ['A', 'B', 'C', 'D', 'E']  # for bar plot
bar_values = np.random.randint(1, 10, size=len(categories))  # for bar plot

# Plotting bar plot
import matplotlib.pyplot as plt
categories=['a','b','c','d','e']
data=[6,8,11,23,16]
plt.figure(figsize=(10,7))
plt.bar(categories,data)
plt.xlabel(data)
plt.ylabel(categories)
plt.show()


# In[ ]:




