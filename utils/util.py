from django.db import models
from dao.sqliteDb import *
# Create your models here.
def getDeviceInfo():
    sd = sqlDao()
    getDeviceInfosql = 'select * from device_info'
    list = sd.getAll(getDeviceInfosql)
    return list


def cleanAlarmUtil(device: str):
    sd = sqlDao()
    if device == 'all':
        cleansql = "update device_info set device_info = 'HEALTH' , fontsize = 20 , btncolor = 'btn-success' "
        p = sd.getAll(cleansql)
        print(p)
