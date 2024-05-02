#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
plt.style.use('bmh')


# In[8]:


df=pd.read_csv("D:\\DSBDA\\Data sets-20240124T042619Z-001\\Data sets\\NFLX.csv")


# In[9]:


print(df.head(6))
print(df.shape)


# In[10]:


plt.figure(figsize=(16,8))
plt.title('Netflix')
plt.xlabel('Days')
plt.ylabel('Close Price USD($)')
plt.plot(df['Close'])
plt.show()


# In[11]:


df = df[['Close']]
print(df.head(4))


# In[12]:


future_days = 50


# In[13]:


df['Prediction'] = df[['Close']].shift(-future_days)
print(df.head(4))
print(df.tail(4))


# In[14]:


x = np.array(df.drop(['Prediction'], 1))[:-future_days]
print(x)


# In[15]:


y = np.array(df['Prediction'])[:-future_days]
print(y)


# In[16]:


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)


# In[17]:


tree = DecisionTreeRegressor().fit(x_train, y_train)


# In[18]:


lr = LinearRegression().fit(x_train, y_train)


# In[19]:


x_future = df.drop(['Prediction'], 1)[:-future_days]
x_future = x_future.tail(future_days)
x_future = np.array(x_future)
print(x_future)


# In[20]:


tree_prediction = tree.predict(x_future)
print(tree_prediction)
print ()


# In[21]:


lr_prediction = lr.predict(x_future)
print(lr_prediction)


# In[22]:


Predictions = tree_prediction
valid = df[x.shape[0]:]
valid['Prediction'] = Predictions
plt.figure(figsize=(16,8))
plt.title('Model_tree')
plt.xlabel('Days')
plt.ylabel('Close Price USD($)')
plt.plot(df['Close'])
plt.plot(valid[['Close', 'Prediction']])
plt.legend(['Orig','Val','Pred'])
plt.show()


# In[23]:


Predictions = lr_prediction
valid = df[x.shape[0]:]
valid['Prediction'] = Predictions
plt.figure(figsize=(16,8))
plt.title('Model_lr')
plt.xlabel('Days')
plt.ylabel('Close Price USD($)')
plt.plot(df['Close'])
plt.plot(valid[['Close', 'Prediction']])
plt.legend(['Orig','Val','Pred'])
plt.show()


# In[ ]:




