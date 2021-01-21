# -*- coding:utf-8 -*-

"""
@File : get_header
@Author : Chen
@Contact : nonevxx@gmail.com
@Date : 2021/1/11 18:34
@Desc : 
"""

import json
import app
from tools.get_log import GetLog

# 获取日志器
log = GetLog.get_log()


# 待废弃, 由get_config代替
def get_header():
    try:
        with open(app.BASE_DIR + "/config/config.json", "r", encoding="utf-8") as f:
            result = json.load(f)
            return result['headers']
    except Exception as ex:
        log.error(ex)


# 待废弃, 由set_submenu代替
def set_token(token):
    try:
        with open(app.BASE_DIR + "/config/config.json", "r", encoding="utf-8") as f:
            result = json.load(f)
            result['headers']['Authorization'] = token

        with open(app.BASE_DIR + "/config/config.json", "w", encoding="utf-8") as f:
            json.dump(result, f)
    except Exception as ex:
        log.error(ex)


def set_config(key, value):
    try:
        with open(app.BASE_DIR + "/config/config.json", "r", encoding="utf-8") as f:
            result = json.load(f)
            result[key] = value

        with open(app.BASE_DIR + "/config/config.json", "w", encoding="utf-8") as f:
            json.dump(result, f)
    except Exception as ex:
        log.error(ex)


def get_config(key):
    try:
        with open(app.BASE_DIR + "/config/config.json", "r", encoding="utf-8") as f:
            result = json.load(f)
            return result[key]
    except Exception as ex:
        log.error(ex)


def get_submenu(key_1, key_2):
    obj = get_config(key_1)
    if key_2 in obj.keys:
        return obj[key_2]
    else:
        return None


def set_submenu(key_1, key_2, value):
    obj = get_config(key_1)
    obj[key_2] = value
    set_config(key_1, obj)


if __name__ == '__main__':
    pass
