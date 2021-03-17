# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 14:51:12 2020

@author: June
"""

from pymongo import MongoClient  

# 連接到local端的MongoDB，MongoDB database使用Robot3T建立
client = MongoClient(host = '127.0.0.1', port = 27017)
db = client['test_db'] # 建立一個data base名為test_db
coll = db['Collections'] # 在test_db中 建立一個collections名為coll
mydata = {'ex_Key': '20200813_test'} # 創建一個字典 my_data
result = coll.insert_one(mydata) # 將my_data添加到coll中

client.list_database_names() # 觀察指定的database裡面的所有collections