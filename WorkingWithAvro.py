#!/usr/bin/env python
# coding: utf-8

# In[1]:


import findspark
findspark.init()


# In[2]:


from pyspark.sql import SparkSession


# In[7]:


spark = SparkSession.builder.appName('Working With Avro Data').master('local[3]')\
.config('spark.driver.host','127.0.0.1')\
.config('spark.ui.port',0).getOrCreate()


# In[8]:


spark.sparkContext.setLogLevel('ERROR')


# In[9]:


df = spark.read.format('avro').load(r'/home/AzureAdmin/data/accounts_avro')
df.printSchema()
df.show()

# In[ ]:




