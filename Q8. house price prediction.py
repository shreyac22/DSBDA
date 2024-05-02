

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# In[2]:


data=pd.read_csv("D:\DSBDA\Data sets-20240124T042619Z-001\Data sets\house.csv")


# In[3]:


print(data.columns) # This will show all the column names
print(data.head(10)) # Show first 10 records of dataframe
print(data.describe()) #You can look at summary of numerical fields by using
print(data.shape)
print(data.isnull().sum())


# In[4]:


sns.relplot(x='median_house_value', y= 'total_bedrooms', data=data)


# In[5]:


sns.relplot(x='median_house_value', y= 'total_rooms', data=data)


# In[6]:


sns.relplot(x='median_house_value', y= 'population', data=data)


# In[7]:


sns.relplot(x='median_house_value', y= 'median_income', data=data)


# In[12]:


sns.relplot(x='median_house_value', y= 'households', data=data)


# In[24]:


sns.relplot(x='median_house_value', y= 'median_income', hue= 'total_rooms',data=data)


# In[26]:


plt.show()


# In[31]:


train =data.drop(['median_house_value','longitude','latitude','housing_median_age'],axis=1)
test =data['median_house_value']


# In[32]:


x_train, x_test, y_train, y_test = train_test_split(train, test, test_size=0.3,random_state=2)


# In[33]:


regr= LinearRegression()
regr.fit(x_train, y_train)
pred = regr.predict(x_test)
print(pred)
print(regr.score(x_test, y_test))


# In[ ]:




