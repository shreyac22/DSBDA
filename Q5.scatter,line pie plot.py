#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()


# In[2]:


plt.plot([1,2,3,4],[1,4,9,16])
plt.show()


# In[3]:


plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.plot([1,2,3,4],[1,4,9,16],'r--')
plt.show()


# In[4]:


import matplotlib.pyplot as plt
import numpy as np
car=['BMW','porshe','juaguar','ford','creta','mercedes']
data=[40,34,28,18,39,50]
fig=plt.figure(figsize=(10,7))
plt.pie(data,labels=car)
plt.show()


# In[5]:


import matplotlib.pyplot as plt
import numpy as np

# Generating sample data
x = np.random.rand(50)  # Random x values
y = np.random.rand(50)  # Random y values

# Plotting scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(x, y)  # Alpha parameter controls transparency
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

plt.show()


# In[ ]:




