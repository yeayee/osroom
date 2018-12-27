# -*-coding:utf-8-*-
import json
from apps.configs.sys_config import APPS_PATH
from apps.core.logger.web_logging import web_start_log
from init_datas import INIT_DATAS

__author__ = 'Allen Woo'


def update_mdb_collections(mdb_sys, mdb_web, mdb_user):

    '''
    更新数据库mongodb collection, 不存在的colletion则创建
    :param mdb_sys:
    :param mdb_web:
    :param mdb_user:
    :return:
    '''

    # 读取配置中的数据库json 数据
    with open("{}/configs/collections.json".format(APPS_PATH)) as rf:
        jsondata = rf.read()
        if jsondata:
            collections = json.loads(jsondata)
        else:
            collections = {}

    dbs = {"mdb_sys":mdb_sys,
           "mdb_user":mdb_user,
           "mdb_web":mdb_web
           }

    # 检查数据库collections
    for dbname,colls in collections.items():
        mdb = dbs[dbname]
        for coll in colls:
            try:
                mdb.dbs.create_collection(coll)
                web_start_log.info("[DB: {}] Create collection '{}'".format(mdb.name, coll))
            except Exception as e:
                if "already exists" in str(e):
                    web_start_log.info(e)
                else:
                    web_start_log.warning(e)

    # 将最新的数据库结构写入配置文件, 方便开发者了解结构
    new_collections = {}
    for dbname, mdb in dbs.items():
        new_collections[dbname] = {}
        collnames = mdb.dbs.collection_names()
        for collname in collnames:
            if collname == "system.indexes" or collname.startswith("plug_"):
                continue
            new_collections[dbname][collname] = {}
            data = mdb.dbs[collname].find_one({},{"_id":0})
            if data:
                for k,v in data.items():
                    new_collections[dbname][collname][k] = str(type(v))

    with open("{}/configs/collections.json".format(APPS_PATH), "w") as wf:
        collections = json.dumps(new_collections, indent=4, ensure_ascii=False)
        wf.write(collections)

def init_datas(mdb_sys, mdb_web, mdb_user):

    '''
    初始web化数据
    :return:
    '''

    for data in INIT_DATAS:

        db = mdb_sys
        if data["db"] == "osr_web":
            db = mdb_web
        elif data["db"] == "osr_user":
            db = mdb_user
        q = {}
        if "condition" in data:
            q = data["condition"]
        if db.dbs[data["coll"]].find_one(q):
            continue
        else:
            print("* [Initialization data] {}".format(data["coll"]))
            db.dbs[data["coll"]].insert_many(data["datas"])
