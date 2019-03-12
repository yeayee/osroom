# -*-coding:utf-8-*-
from flask import request

from apps.app import mdb_web
from apps.core.utils.get_config import get_config
from apps.utils.format.obj_format import json_to_pyseq

__author__ = 'Allen Woo'

def get_tags():
    '''
    根据条件获取post tags
    :return:
    '''
    sort = json_to_pyseq(request.argget.all('sort'))
    # sort
    if sort:
        for i in range(0, len(sort)):
            sort[i] = (list(sort[i].keys())[0], list(sort[i].values())[0])
    else:
        sort = [("issue_time", -1), ("update_time", -1)]

    query_conditions = {}
    query_conditions['issued'] = 1
    query_conditions['is_delete'] = 0
    query_conditions['audit_score'] = {"$lt": get_config("content_inspection", "ALLEGED_ILLEGAL_SCORE")}
    mdb_web.db.post.find(query_conditions, {"tags":1}).sort(sort).limit()