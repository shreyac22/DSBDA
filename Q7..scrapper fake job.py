#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
print(page.text)


# In[3]:


soup = BeautifulSoup(page.content, "html.parser")


# In[4]:


results = soup.find(id="ResultsContainer")
print(results.prettify())


# In[5]:


job_elements = results.find_all("div", class_="card-content")


# In[6]:


for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")


# In[7]:


print(title_element)


# In[8]:


print(company_element)


# In[9]:


print(location_element)


# In[10]:


print()


# In[11]:


print(title_element.text)


# In[12]:


print(company_element.text)


# In[13]:


print(location_element.text)


# In[14]:


print()


# In[16]:


print("Title of Job =",title_element.text.strip())


# In[17]:


print("Company Name =",company_element.text.strip())


# In[19]:


print("Location of Job =",location_element.text.strip())


# In[21]:


python_jobs = results.find_all("h2", string="Python")
print(python_jobs)


# In[22]:


python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
print("Number of Jobs in Python =", len(python_jobs))
print(len(python_jobs))


# In[ ]:




