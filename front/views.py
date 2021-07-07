from django.shortcuts import render
from dao.mongodbConn import MongoDao
from django.http import JsonResponse
from django.http import HttpResponse
from utils.util import *
from django.shortcuts import redirect
# homepage
from config import *
from dao.sqliteDb import *

def front(request):

    # 获取Device info
    # deviceinfolist = getDeviceInfo()
    # 获取temp list
    mdb = MongoDao()
    gputemp = []

    # 获取gpu info
    gpuinfoList = getGpuInfo()
    # 获取 switch info
    SwitchInfolist = getSwitchInfo()
    # 获取 power meter
    powerMeterInfoList = getPowerInfo()

    # 获取 gpu temp
    for i in gpuinfoList:
        # print(i)
        temp = mdb.selectLast(i[1]+'Temp',1)
        gputemp.append([i[1] , temp[0]['temp']])
    # 获取 gpupower
    powerMeter = []
    for i in powerMeterInfoList:
        power = mdb.selectLast('Power'+str(i[0]),1)
        powerMeter.append([i[0],power[0]['power'] ,i[2]])

    print(powerMeter)

    # 获取 switch temp
    switchTemp = []
    for i in SwitchInfolist:
        # print(i)
        temp = mdb.selectLast(i[1]+'Temp',1)
        switchTemp.append([i[1] , temp[0]['temp']])


    return render(request,'home.html',{'gpuinfo': gpuinfoList,'SwitchInfo':SwitchInfolist,'gputemp':gputemp,'switchTemp':switchTemp,'powerMeter':powerMeter})


# 清除报警信息
def cleanAlarm(request):
    sd = sqlDao()
    # cleansql = """ update device_info set deviceinfo = ? , fontsize = ? , btncolor = ?  """

    cleanGpusql = """update gpu_info set gpu_status = ? , btn_color = ?   """
    cleanSwitchsql = """update switch_info set switch_status = ? , btn_color = ?   """
    cleanPowersql = 'update power_meter_info set power_status = ? , btn_color = ? '
    args = [HEALTH_sign,HEALTH_btn_color]

    sd.getOneP(cleanGpusql,args)
    sd.getOneP(cleanSwitchsql,args)
    sd.getOneP(cleanPowersql,args)
    sd.closeConn()
    return redirect('/home')

# 废弃
def getHomePageStatus(request):

    #获取当前数据库信息
    sd = sqlDao()
    getStatusSql= 'select * from device_info'
    list = sd.getAll(getStatusSql)
    # print(list.__class__)
    # print(list)
    jsonData={'data' : list}
    # print(jsonData)
    return JsonResponse(jsonData)

def getGpuStatus(request):

    #获取当前数据库信息
    sd = sqlDao()
    getStatusSql= 'select * from gpu_info'
    list = sd.getAll(getStatusSql)
    # print(list.__class__)
    # print(list)
    jsonData={'data' : list}
    # print(jsonData)
    return JsonResponse(jsonData)


def getGpuTemp(request):
    gpuList = getGpuInfo()
    # print(gpuList)
    tempList = []
    mdb = MongoDao()
    for i in gpuList:
        # print(i[1])
        tempList.append([i[1],mdb.selectLast(i[1]+'Temp',1)[0]['temp']])
    # 查询最后一条温度信息
    # print(tempList)
    # temp=mdb.selectLast('inventec', 1)
    # temp = temp[0]
    tempList={'temp':tempList}
    return JsonResponse(tempList)


def getPower(request):
    powerMeterList = getPowerInfo()
    # print(gpuList)
    powerList = []
    mdb = MongoDao()
    for i in powerMeterList:
        # print(i[2])
        # print(mdb.selectLast( 'Power'+str(i[0]), 1)[0]['power'])
        powerList.append([ 'Power'+str(i[0]),mdb.selectLast('Power'+str(i[0]),1)[0]['power'] , i[2]])

    powerList={'power':powerList}
    # print(powerList)
    return JsonResponse(powerList)


def getSwitchTemp(request):
    gpuList = getSwitchInfo()
    # print(gpuList)
    tempList = []
    mdb = MongoDao()
    for i in gpuList:
        # print(i[1])
        tempList.append([i[1],mdb.selectLast(i[1]+'Temp',1)[0]['temp']])
    # 查询最后一条温度信息
    # print(tempList)
    # temp=mdb.selectLast('inventec', 1)
    # temp = temp[0]
    tempList={'temp':tempList}
    return JsonResponse(tempList)

def getSwitchStatus(request):

    #获取当前数据库信息
    sd = sqlDao()
    getStatusSql= 'select * from switch_info'
    list = sd.getAll(getStatusSql)
    # print(list.__class__)
    # print(list)
    jsonData={'data' : list}
    # print(jsonData)
    return JsonResponse(jsonData)
