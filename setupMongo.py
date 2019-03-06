# _*_ coding:utf-8 _*_
import os
# 启动mongo
def startMongo():
    os.system('cd /config/mongod/docker && docker-compose up -d')
startMongo()