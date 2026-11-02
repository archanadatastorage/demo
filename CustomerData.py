#!/usr/bin/env python
# coding: utf-8

# In[1]:


import findspark
findspark.init()


# In[2]:


from pyspark.sql import SparkSession


# In[3]:


spark = SparkSession.builder.appName("customer code").master('local[3]').config('spark.driver.host','127.0.0.1')\
.config('spark.ui.port',0).getOrCreate()


# In[4]:


spark.sparkContext.setLogLevel('ERROR')


# In[30]:


PM = spark.read.format('csv')\
.option('header',True).option('inferSchema',True)\
.load(r'/home/AzureAdmin/Dataset_01/Baseband_02/Dataset_01_LTE_2100.csv')


# In[31]:


PM.printSchema()


# In[11]:


PM.count()


# In[12]:


type(PM)


# In[32]:


PM.createOrReplaceTempView('PerMgmt')


# In[20]:


spark.catalog.listTables()


# In[17]:


#spark.catalog.dropTempView('PerMgmt')


# In[27]:


spark.sql('select Sector,count(*) as cnt from PerMgmt group by Sector having cnt > 2000 order by cnt desc').show()


# In[29]:


PM.select('Base station').distinct().show()


# In[47]:


spark.sql("select Sector, count(*) over(partition by Sector) as cnt from PerMgmt ").show()


# In[48]:


spark.sql("select `Base station`, count(*) over(partition by `Base station`) as cnt from PerMgmt").show()


# In[ ]:




