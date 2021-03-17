# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 19:25:08 2020

@author: June
"""

from pymongo import MongoClient  
import requests
import base64

# 連接到local端的MongoDB，MongoDB database使用Robot3T建立
client = MongoClient(host = '127.0.0.1', port = 27017)
db = client['yolo_pred_db'] # 建立一個data base 命名為yolo_pred_db
coll = db['Collections'] # 在test_db中 建立一個collections，透過coll變數呼叫他

# 從flask取得推論結果
r = requests.get('http://10.17.4.132:8080')
if r.status_code == requests.codes.ok:
    print(r.text)
yolo_result = r.text

# 從flask端取得影像
url = 'http://10.17.4.132:8080' # 指定flask web的位址
index_url = url+'/index' # 指定web中影像的位址 (影像被放在inex目錄下)

head = res.find('<img src=') # 取得影像物件的html敘述的開頭index
tail = head+res[head:].find('>') # 取得影像物件的html敘述的結尾index
img_url = url+res[head:tail].split('\"')[1] # 透過頭尾index來取得影像的具體位址
print(img_url) 
img_name = 'prediction.jpg'

html = requests.get(img_url)
with open(img_name, 'wb') as file:
    file.write(html.content)

# 上傳到mongoDB

# 連接到local端的MongoDB，MongoDB database使用Robot3T建立
client = MongoClient(host = '127.0.0.1', port = 27017)
db = client['yolo_pred_db'] # 建立一個data base名為test_db
coll = db['Collections'] # 在test_db中 建立一個collections名為coll
    
with open(img_name, "rb") as f: #使用python內建的檔案讀寫工具open
    bin_pic = base64.b64encode(f.read()).decode('utf-8') # 將讀取到的圖片(f)編碼成二進制檔
    # image_data = {'jpg_base64': strpic} # 將jpg_base64這個key和二進制化的圖片編成一組字典my_data
    # result = coll.insert_one(mydata) # 在coll裡面新增my_data
    # print(result.inserted_id) # 打印出my_data在儲存時，DB分配出來的id
    mydata = {'yolo_result': yolo_result, 'image_data': bin_pic}
    result = coll.insert_one(mydata)
    
with open("imageList.txt", "a+") as file: # 編輯imageList.txt文件。不存在則創建之
    old = file.read() # read everything in the file # 讀取imageList.txt
    file.seek(0) # rewind
    content = '%\n'+img_name+'\n'+str(result.inserted_id) # 將圖片名和id整合到變數content中
    # 接著將content儲存到imageList.txt中
    file.write(content+"\n" + old) # write the new line before 
    


