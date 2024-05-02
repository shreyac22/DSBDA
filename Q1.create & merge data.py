#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


data={'roll-no':[10,20,30,40,50,60,70],'name':['alina','jiya','siri','john','alok','mini','jini'],'age':[12,14,13,12,14,13,15]}


# In[6]:


data=pd.DataFrame(data)


# In[7]:


print("Original dataframe: \n")


# In[8]:


print(data)


# In[9]:


print(data.loc[[0,1,3]])


# In[10]:


print(data.loc[0:3])


# In[11]:


print(data.loc[0:2,['age','name']])


# In[12]:


print(data.iloc[[0,1,3,6],[0,2]])


# In[13]:


#merging


# In[14]:


import pandas as pd


# In[15]:


d1={'name':['pankaj','sachin','bob'],'country':['india','india','USA'],'role':['CEO','CTO','CTO']}


# In[16]:


df1=pd.DataFrame(d1)


# In[17]:


print("DataFrame 1 : \n")


# In[18]:


print(df1)


# In[19]:


d2={'id':[1,2,3],'name':['pankaj','alina','mona']}


# In[20]:


df2=pd.DataFrame(d2)


# In[21]:


print("DataFrame 2 : \n")


# In[22]:


print(df1)


# In[23]:


df_merged=df1.merge(df2)


# In[24]:


print('Result inner join \n:',df_merged)


# In[25]:


print('Result left join : \n',df1.merge(df2,how='left'))


# In[26]:


print('Result right join : \n',df1.merge(df2,how='right'))


# In[28]:


print('Result outer join : \n',df1.merge(df2,how='outer'))


# In[ ]:




