# -*- coding:utf-8 -*-

"""
@File : template_api
@Author : Chen
@Contact : nonevxx@gmail.com
@Date : 2021/1/20 16:54
@Desc : 
"""

# 导包
import app
import json
from tools.config_info import get_header


class TemplateAPI:
    # xx添加接口
    api_add_url = app.BASE_URL + "/xxx/xxxx/add"
    # xx修改接口
    api_upd_url = app.BASE_URL + "/xxx/xxxx/upd"
    # xx查询接口
    api_get_url = app.BASE_URL + "/xxx/xxxx/get"
    # xx删除接口
    api_del_url = app.BASE_URL + "/xxx/xxxx/del/{id}"

    # xx添加接口函数实现
    def api_add(self, session, attr1, attr2):
        post_data = {
            "attr1": attr1,
            "attr2": attr2
        }
        return session.post(self.api_add_url, headers=get_header(), data=json.dumps(post_data))

    # xx修改接口函数实现
    def api_upd(self, session, attr1, attr2):
        put_data = {
            "attr1": attr1,
            "attr2": attr2
        }
        return session.put(self.api_upd_url, headers=get_header(), data=json.dumps(put_data))

    # xx查询接口函数实现
    def api_get(self, session, attr1, attr2):
        params = {
            "attr1": attr1,
            "attr2": attr2
        }
        return session.get(self.api_get_url, headers=get_header(), params=params)

    # xx删除接口函数实现
    def api_del(self, session, uid):
        return session.delete(self.api_del_url.format(id=uid), headers=get_header())
