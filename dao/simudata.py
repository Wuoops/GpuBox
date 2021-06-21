import time

from dao.mongodbConn import MongoDao
from utils.util import *
import random
from dao.sqliteDb import *
import config

def getTemp():
#     获取device_info表信息
    list = getDeviceInfo()
    # print(list)
    mdb = MongoDao()

    for i in list:
        print(i[1])
        temp = random.randint(500, 700) / 10
        mdb.insertOneData(i[1],{'temp':temp,'time':time.time()})


def changeStatus():
    sd  = sqlDao()
    limitsql = 'select * from m_limit'
    limitList = sd.getAll(limitsql)



    pass


# 根据设备信息写入数据
# getTemp()



for i in (range(100)):
    time.sleep(1) ;
    getTemp()




