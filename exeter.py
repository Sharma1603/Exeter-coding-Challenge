#!/usr/bin/env python
# coding: utf-8

# In[229]:


#LIBRARY
import pandas as pd


# <b>FOR EXTENDING DISPLAY OPTION<b>

# In[230]:


pd.set_option('display.max_columns',None)


# In[231]:


pd.set_option('display.max_rows',None)


# In[232]:


textfile=pd.read_table(r"C:\Users\nicks\Desktop\t8.shakespeare.txt")


# In[233]:


textfile


# <b>FOR DISPLAYING WORDS IN FIND_WORDS LIST<b>

# In[234]:


findwords=pd.read_table(r"C:\Users\nicks\Desktop\find_words.txt")


# In[235]:


findwords


# <b>FOR DISPLAYING FRENCH WORDS IN DICTIONARY<b>

# In[236]:


dictionary=pd.read_csv(r"C:\Users\nicks\Desktop\french_dictionary.csv",usecols=['respecter'])


# In[237]:


dictionary


# <b>FOR REPLACING WORDS OF FIND_WORDS TEXT FILE WITH FRENCH WORDS OF DICTIONARIES<b>

# In[238]:


a=dictionary.replace(to_replace='txtfile',value='dictionary')


# In[239]:


a


# <b>FOR COUNTING TIME TAKEN TO PROCESS AND NUMBER OF TIMES WORD IS REPLACED<b>

# In[242]:


get_ipython().run_cell_magic('time', '', "count=a['respecter'].value_counts()\ncount")


# <b>MEMORY TAKEN TO PROCESS<b>

# In[243]:


import os,psutil
pid=os.getpid()
print(pid)
ps=psutil.Process(pid)
#getmemoryUsageInfo
memoryuse=ps.memory_info()
print(memoryuse)

