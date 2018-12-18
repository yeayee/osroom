# -*-coding:utf-8-*-
from apps.configs.mdb_collection import collections
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

    dbs = {"mdb_sys":mdb_sys,
           "mdb_user":mdb_user,
           "mdb_web":mdb_web
           }

    for k,colls in collections.items():
        mdb = dbs[k]
        for coll in colls:
            try:
                mdb.dbs.create_collection(coll)
                web_start_log.info("[DB: {}] Create collection '{}'".format(mdb.name, coll))
            except Exception as e:
                if "already exists" in str(e):
                    web_start_log.info(e)
                else:
                    web_start_log.warning(e)

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
