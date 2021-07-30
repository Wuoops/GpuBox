import time

from dao.mongodbConn import MongoDao
from utils.util import *
import random
from dao.sqliteDb import *
from config import *


def getTemp():
#     获取device_info表信息
    list = getDeviceInfo()
    # print(list)
    mdb = MongoDao()


    for i in list:
        # print(i[1])
        temp = random.randint(500, 700) / 10
        mdb.insertOneData(i[1],{'temp':temp,'time':time.time()})

        if temp >= i[3] and temp < i[6]:
            changeStatus(int(i[0]),'WARNNG')
            # print(temp)
        elif temp >= i[6]:
            changeStatus(int(i[0]),'DANGER')
            # print(temp)
# 弃用
def changeStatus(id,status):
    sd = sqlDao()
    changeSql = 'update device_info set deviceinfo = ? , fontsize = ?, btncolor = ? where device_id = ?'
    # changeSql = 'update device_info set deviceinfo = ? , fontsize = ?, btncolor = ? where device_id = ?'
    if status == 'WARNNG':
        args = [WARNNG_sign,WARNNG_font_size,WARNNG_btn_color,id]
    elif status == 'DANGER':
        args = [DANGER_sign,DANGER_font_size,DANGER_btn_color,id]

    sd.modifyP(changeSql,args)
    sd.closeConn()


#######
# 修改GPU状态表
def changeGpuStatus(id,status):
    sd = sqlDao()
    changeSql = 'update gpu_info set gpu_status = ? , btn_color = ? where id = ?'

    if status == 'WARNNG':
        args = [WARNNG_sign,WARNNG_btn_color,id]
    elif status == 'DANGER':
        args = [DANGER_sign,DANGER_btn_color,id]
    sd.modifyP(changeSql,args)
    sd.closeConn()

def changeSwitchStatus(id,status):
    sd = sqlDao()
    changeSql = 'update switch_info set switch_status = ? , btn_color = ? where id = ?'

    if status == 'WARNNG':
        args = [WARNNG_sign,WARNNG_btn_color,id]
    elif status == 'DANGER':
        args = [DANGER_sign,DANGER_btn_color,id]
    sd.modifyP(changeSql,args)
    sd.closeConn()

def changePowerMeterStatus(id,status):
    sd = sqlDao()
    changeSql = 'update power_meter_info set power_status = ? , btn_color = ? where id = ?'

    if status == 'WARNNG':
        args = [WARNNG_sign,WARNNG_btn_color,id]
        print(args)
    elif status == 'DANGER':
        args = [DANGER_sign,DANGER_btn_color,id]
    sd.modifyP(changeSql,args)
    sd.closeConn()

def insertGpuTemp():
    # 获取gpulist
    list = getGpuInfo()
    # 获取limit
    limit = getLimit("GPU")
    temp_warning = limit[1]
    temp_danger = limit[2]

    mdb = MongoDao()
    for i in list:
        # print(i[1])
        temp = random.randint(500, 700) / 10
        mdb.insertOneData(i[1]+'Temp',{'temp':temp,'time':time.time()})
        if temp >= temp_warning and temp < temp_danger:
            changeGpuStatus(int(i[0]),'WARNNG')
            # print(temp)
        elif temp >= temp_danger:
            changeGpuStatus(int(i[0]),'DANGER')
            # print(temp)

# 插入 power数据
def insertPower():
    # 获取gpulist
    list = getPowerInfo()
    # 获取limit
    limit = getLimit("GPU")
    power_warning = limit[3]
    power_danger = limit[4]
    print(power_warning)
    mdb = MongoDao()
    for i in list:
        # print(i[1])
        power = random.randint(500, 700)
        print(power)
        mdb.insertOneData('Power'+str(i[0]),{'power':power,'time':time.time()})
        if power >= power_warning and power < power_danger:
            changePowerMeterStatus(int(i[0]),'WARNNG')
            print(power)
        elif power >= power_danger:
            changePowerMeterStatus(int(i[0]),'DANGER')
            print(power)


# 获取switch温度
def insertSwitchTemp():
    # 获取switch list
    list = getSwitchInfo()
    # 获取limit
    limit = getLimit("SWITCH")
    temp_warning = limit[1]
    temp_danger = limit[2]

    mdb = MongoDao()
    for i in list:
        # print(i[1])
        temp = random.randint(500, 700) / 10
        mdb.insertOneData(i[1] + 'Temp', {'temp': temp, 'time': time.time()})
        if temp >= temp_warning and temp < temp_danger:
            changeSwitchStatus(int(i[0]), 'WARNNG')
            print(temp)
        elif temp >= temp_danger:
            changeSwitchStatus(int(i[0]), 'DANGER')
            # print(temp)



def insertSwitchPower():
    pass

# 获取limit
def getLimit(deviceType):
    sd = sqlDao()
    getlimitSql = ''' select * from  m_limit where device_type = ? '''
    args = [deviceType,]
    limit = sd.getOneP(getlimitSql,args)
    # temp_warning = limit[1]
    # temp_danger = limit[2]
    # power_warning = limit[3]
    # power_danger = limit[4]
    # print(limit)
    return limit


def start():
    sd = sqlDao()
    getLinesSql = 'select lines from simdata'
    lines = sd.getOne(getLinesSql)
    print(lines[0])
    for i in (range(lines[0])):
        time.sleep(1) ;
        insertGpuTemp()
        insertSwitchTemp()
        insertPower()
# start()
