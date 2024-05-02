#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


csvData = pd.read_csv("C:\\Users\\shrey\\Downloads\\records.csv")


# In[3]:


print("\nBefore sorting:")


# In[4]:


print(csvData)


# In[5]:


csvData.sort_values(["Salary"], axis=0, ascending=[False], inplace=True)


# In[6]:


csvData.sort_values(["Salary"],axis=0, ascending=[True], inplace=True)


# In[7]:


print("\nAfter sorting:")


# In[8]:


print(csvData)


# In[9]:


#Transpose
import pandas as pd


# In[10]:


df= pd.read_csv("C:\\Users\\shrey\\Downloads\\records.csv")


# In[11]:


print(df)


# In[12]:


print(df.T)


# In[13]:


print(df.shape)


# In[14]:


print(df.size)


# In[15]:


#Shape
import pandas as pd


# In[16]:


df= pd.read_csv("C:\\Users\\shrey\\Downloads\\records.csv")


# In[17]:


print(df)


# In[18]:


print(df.shape)


# In[19]:


print(df.size)


# In[ ]:




