from django.test import TestCase
from dao.mongodbConn import *
# Create your tests here.
# 查询最后一条温度信息
import json
from json import dumps

mdb = MongoDao()
temp = mdb.selectLast('inventec', 1)[0]
temp = dumps(temp)
print(temp)