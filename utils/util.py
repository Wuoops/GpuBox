from django.db import models
from dao.sqliteDb import *
# Create your models here.

# 废弃方法
def getDeviceInfo():
    sd = sqlDao()
    getDeviceInfosql = 'select * from device_info'
    list = sd.getAll(getDeviceInfosql)
    return list


def getGpuInfo():
    sd = sqlDao()
    getgpuinfosql = 'select * from gpu_info '
    list = sd.getAll(getgpuinfosql)
    return list


def getSwitchInfo():
    sd = sqlDao()
    getgpuinfosql = 'select * from switch_info '
    list = sd.getAll(getgpuinfosql)
    return list


def getPowerInfo():
    sd = sqlDao()
    getPowerinfosql = 'select * from power_meter_info'
    list = sd.getAll(getPowerinfosql)
    return list
def cleanAlarmUtil(device: str):
    sd = sqlDao()
    if device == 'all':
        cleansql = "update device_info set device_info = 'HEALTH' , fontsize = 20 , btncolor = 'btn-success' "
        p = sd.getAll(cleansql)
        print(p)



