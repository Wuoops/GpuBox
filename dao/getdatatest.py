from dao.mongodbConn import MongoDao

mdb = MongoDao()
print(mdb.selectLast('inventec',1))





