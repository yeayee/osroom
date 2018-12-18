# -*-coding:utf-8-*-
import math
from bson import ObjectId
from flask import request
from flask_babel import gettext
from flask_login import current_user

from apps.configs.sys_config import SUPER_PER
from apps.core.flask.reqparse import arg_verify
from apps.utils.format.number import get_num_digits
from apps.utils.format.obj_format import objid_to_str, json_to_pyseq, str_to_num
from apps.utils.paging.paging import datas_paging
from apps.app import mdb_user, cache

__author__ = "Allen Woo"


def permission():
    '''
    获取一个权限
    :return:
    '''
    id = request.argget.all('id').strip()
    data = {}
    data["per"] = mdb_user.db.permission.find_one({"_id":ObjectId(id)})
    if not data["per"]:
        data = {'msg':gettext("The specified permission is not found"), 'msg_type':"w", "http_status":404}
    else:
        data["per"]["_id"] = str(data["per"]["_id"])
        data["per"]["pos"] = get_num_digits(data["per"]["value"])

    return data


def permissions_details():

    '''
    获取多个权限的详情
    :return:
    '''

    data = {}
    page = int(request.argget.all('page', 1))
    pre = int(request.argget.all('pre', 10))
    rs = mdb_user.db.permission.find({})
    data_cnt = rs.count(True)
    roles = list(rs.skip(pre*(page-1)).limit(pre))
    roles = sorted(roles, key=lambda x:x["value"])
    for role in roles:
        role["pos"] = get_num_digits(role["value"])
    data["pers"] = datas_paging(pre=pre, page_num=page, data_cnt = data_cnt, datas = objid_to_str(roles))

    return data

def permissions():

    '''
    只获取name,value, explain,以及已使用的权重位置
    :return:
    '''

    data = []
    positions = list(range(1, get_num_digits(SUPER_PER)+1))
    for per in mdb_user.dbs["permission"].find({"value":{"$exists":True}}).sort([("value",-1)]):
        temp_pos = get_num_digits(per["value"])
        if temp_pos in positions:
            positions.remove(temp_pos)
        data.append((per["name"],per["value"],per["explain"]))
    data = {"permissions":sorted(data, key=lambda x:x[1]), "positions":positions}
    return data

def add_per():

    name = request.argget.all('name','').strip()
    explain = request.argget.all('explain')
    default = int(request.argget.all('is_default', 0).strip())
    position = str_to_num(request.argget.all('position',0))
    data = {'msg':gettext("Add a success"), 'msg_type':"s", "http_status":201}

    s, r = arg_verify(reqargs=[(gettext("name"), name), (gettext("position"), position)],
                      required=True)
    if not s:
       return r

    hightest_pos = get_num_digits(SUPER_PER)
    permissions = int(math.pow(2, position - 1))
    if hightest_pos > 32 and position<1:
        data = {'msg': gettext("Must be an integer greater than 0,"
                               " less than or equal to {}".format(hightest_pos)),
                'msg_type': "w", "http_status": 403}

    elif mdb_user.db.permission.find_one({"name":name}):
        data = {'msg': gettext("Permission name or valready exists"),
                'msg_type': "w", "http_status": 403}

    elif mdb_user.db.permission.find_one({"value":permissions}):
        data = {'msg': gettext('Location has been used'),
                'msg_type': "w", "http_status": 403}
    else:
        user_role = mdb_user.db.role.find_one({"_id":ObjectId(current_user.role_id)})
        if get_num_digits(user_role["permissions"]) <= get_num_digits(permissions):
            data = {"msg":gettext("The current user permissions are lower than the permissions that you want to add,"
                                                  " without permission to add"),
                    "msg_type":"w","http_status":401}
            return data

        mdb_user.db.permission.insert_one({"name":name,
                                "explain":explain,
                                'value':permissions,
                                "is_default":default})
        cache.delete(key="sys_permissions_default", db_type="redis")
        cache.delete(key="sys_permissions", db_type="redis")
    return data

def edit_per():

    id = request.argget.all('id').strip()
    name = request.argget.all('name','').strip()
    explain = request.argget.all('explain','')
    default = int(request.argget.all('is_default', 0).strip())
    position = str_to_num(request.argget.all('position', 0))

    s, r = arg_verify(reqargs=[(gettext("name"), name), (gettext("position"), position)],
                      required=True)
    if not s:
        return r

    hightest_pos = get_num_digits(SUPER_PER)
    if position > hightest_pos and position < 1:
        data = {'msg': gettext("Must be an integer greater than 0,"
                               " less than or equal to {}".format(hightest_pos)),
                'msg_type': "w", "http_status": 403}

        return data
    data = {"msg": gettext("The current user permissions are lower than the permissions you want to modify,"
                           " without permission to modify"),
            "msg_type": "w", "http_status": 401}
    user_role = mdb_user.db.role.find_one({"_id":ObjectId(current_user.role_id)})

    # 如果当前用户的权限最高位 小于 要修改成的这个角色权重的最高位,是不可以的
    permissions = int(math.pow(2, position - 1))
    if get_num_digits(user_role["permissions"]) <= get_num_digits(permissions):

        return data

    per = {"name":name,
            "explain":explain,
            'value':permissions,
            "is_default":default}

    data = {'msg': gettext("Save success"), 'msg_type': "s", "http_status": 201}
    if mdb_user.db.permission.find_one({"name":name, "_id":{"$ne":ObjectId(id)}}):
        data = {'msg': gettext("Permission name already exists"), 'msg_type': "w",
                "http_status": 403}

    elif mdb_user.db.permission.find_one({"value":permissions, "_id":{"$ne":ObjectId(id)}}):
        data = {'msg': gettext('Location has been used'),
                'msg_type': "w", "http_status": 403}
        cache.delete(key="sys_permissions_default", db_type="redis")
        cache.delete(key="sys_permissions", db_type="redis")
    else:
        r = mdb_user.db.permission.update_one({"_id":ObjectId(id)}, {"$set":per})
        if not r.modified_count:
            data = {'msg':gettext("No changes"), 'msg_type':"w", "http_status":201}
    return data

def delete_per():

    ids = json_to_pyseq(request.argget.all('ids'))

    user_role = mdb_user.db.role.find_one({"_id":ObjectId(current_user.role_id)})
    noper = 0
    for id in ids:
        id = ObjectId(id)
        # 权限检查
        old_per = mdb_user.db.permission.find_one({"_id":id})
        # 如果当前用户的权限最高位 小于 要删除角色的权限,也是不可以
        if old_per and get_num_digits(old_per["value"]) >= get_num_digits(user_role["permissions"]):
            noper += 1
            continue

        mdb_user.db.permission.delete_many({"_id":id, "name":{"$nin":["GENERAL_USER","ROOT", "ADMIN", "STAFF"]}})

    if not noper:
        data = {'msg':gettext('Successfully deleted'),
                'msg_type':'s', "http_status":204}
    else:
        data = {'msg':gettext('Successfully deleted, and {} have no permission to delete').format(noper),
                'msg_type':'w', "http_status":400}
    cache.delete(key="sys_permissions_default", db_type="redis")
    cache.delete(key="sys_permissions", db_type="redis")
    return data