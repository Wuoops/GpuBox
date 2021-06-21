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
    deviceinfolist = getDeviceInfo()
    # 获取temp list
    mdb = MongoDao()
    templist = []

    for i in deviceinfolist:
        print(i)
        temp = mdb.selectLast(i[1],1)
        templist.append([i[1] , temp[0]['temp']])

    return render(request,'home.html',{'deviceinfo': deviceinfolist,'templist':templist})


def getHomepageTempData(request):

    deviceinfolist = getDeviceInfo()
    print(deviceinfolist)
    tempList = []
    mdb = MongoDao()
    for i in deviceinfolist:
        print(i[1])
        tempList.append([i[1],mdb.selectLast(i[1],1)[0]['temp']])
    # 查询最后一条温度信息
    print(tempList)
    # temp=mdb.selectLast('inventec', 1)
    # temp = temp[0]
    tempList={'temp':tempList}
    return JsonResponse(tempList)

# 清除报警信息
def cleanAlarm(request):
    sd = sqlDao()
    cleansql = """ update device_info set deviceinfo = ? , fontsize = ? , btncolor = ?  """
    args = [HEALTH_sign,HEALTH_font_size,HEALTH_btn_color]
    # print(args)
    print(sd.getAllP(cleansql,args))
    sd.closeConn()
    return redirect('/home')


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