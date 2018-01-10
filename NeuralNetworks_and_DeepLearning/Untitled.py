
# coding: utf-8

# In[1]:

from pymongo import MongoClient


cluster_uri = 'mongodb://m001-student:m001-mongodb-basics@cluster0-shard-00-00-jxeqq.mongodb.net:27017,cluster0-shard-00-01-jxeqq.mongodb.net:27017,cluster0-shard-00-02-jxeqq.mongodb.net:27017/?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin'

client = MongoClient(cluster_uri)


# In[ ]:



