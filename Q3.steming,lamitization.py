#!/usr/bin/env python
# coding: utf-8

# In[26]:


punctuations = '''!()-{}[];:"'\,<>./?@#$%^&*_~`'''


# In[27]:


my_str = "Hello!!!, he said ...and went."


# In[28]:


no_punct = ""


# In[29]:


for char in my_str:
  if(char not in punctuations):
      no_punct = no_punct + char
      print(no_punct)


# In[30]:


# Data cleaning 2
import re
s = "Hello!!!, he said ...and went."
s = re.sub(r'[^\w\s]','',s)
# not of word and space character
print(s)


# In[31]:


import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
print(stop_words)


# In[35]:


import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer()
input_str = "There are several types of stemming algorithms."
input_str = nltk.word_tokenize(input_str)
print (input_str)
for word in input_str:
  print(stemmer.stem(word))


# In[36]:


import nltk


# In[37]:


nltk.download('omw-1.4')


# In[38]:


import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
lemmatizer = WordNetLemmatizer()
input_str = "There are several cities with mice."
input_str = nltk.word_tokenize(input_str)
print (input_str)
for word in input_str:
  print(lemmatizer.lemmatize(word))






