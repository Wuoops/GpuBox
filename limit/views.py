from django.shortcuts import render
from django.http import HttpResponse
from dao.sqliteDb import sqlDao
# Create your views here.
from dao.simudata import *
import time
from threading import Thread

def setlimit(request):
    sd = sqlDao()

    if request.GET:
        reqGet = request.GET
        gpuTempWarning=reqGet.get('gpuTempWarning')
        gpuTempDanger=reqGet.get('gpuTempDanger')
        gpuPowerWarning=reqGet.get('gpuPowerWarning')
        gpuPowerDanger=reqGet.get('gpuPowerDanger')
        switchTempWarning=reqGet.get('switchTempWarning')
        switchTempDanger=reqGet.get('switchTempDanger')


        updategpuSql = 'update m_limit set temp_warning = ? , \
                    temp_danger = ? , power_warning = ? , power_danger = ? where device_type = "GPU"'
        updateSwitchSql = 'update m_limit set temp_warning = ? , \
                    temp_danger = ? where device_type = "SWITCH"'

        sd.modifyP(updategpuSql,[gpuTempWarning,gpuTempDanger,gpuPowerWarning,gpuPowerDanger])
        sd.modifyP(updateSwitchSql,[switchTempWarning,switchTempDanger])
        sd.closeConn()


    sd = sqlDao()

    getLimitsql = 'select * from m_limit'
    limitList = sd.getAll(getLimitsql)
    gpuTempWarning=limitList[0][1]
    gpuTempDanger=limitList[0][2]
    gpuPowerWarning=limitList[0][3]
    gpuPowerDanger=limitList[0][4]
    switchTempWarning=limitList[1][1]
    switchTempDanger=limitList[1][2]


    return render(request,'limit.html',{'gpuTempWarning':gpuTempWarning,
                                        'gpuTempDanger':gpuTempDanger,
                                        "gpuPowerWarning":gpuPowerWarning,
                                        'gpuPowerDanger':gpuPowerDanger,
                                        'switchTempWarning':switchTempWarning,
                                        'switchTempDanger':switchTempDanger})



def simdatda(request):
    t1 = Thread(target=start)
    t1.start()
    return HttpResponse('started')