#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


df=pd.read_csv("D:\\DSBDA\\Data sets-20240124T042619Z-001\\Data sets\\records.csv")


# In[4]:


df.head()


# In[5]:


print(df)


# In[6]:


df.info()


# In[7]:


updated_df = df.dropna(axis=1)
print(updated_df)
updated_df.info()


# In[8]:


updated_df = df.dropna(axis=0)
print(updated_df)
updated_df.info()


# In[9]:


updated_df = df
updated_df['Salary']=updated_df['Salary'].fillna(updated_df['Salary'].mean())
print(updated_df)


# In[10]:


updated_df = df
updated_df['Salaryismissing'] = updated_df['Salary'].isnull()
print(updated_df)


# In[11]:


testdf = df[df['Salary'].isnull()==True]
traindf = df[df['Salary'].isnull()==False]
traindf.drop("Salary",axis=1,inplace=True)
testdf.drop("Salary",axis=1,inplace=True)
print(traindf)


# In[ ]:




