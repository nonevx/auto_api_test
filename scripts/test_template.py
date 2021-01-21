# -*- coding:utf-8 -*-

"""
@File : test_template
@Author : Chen
@Contact : nonevxx@gmail.com
@Date : 2021/1/20 20:09
@Desc : 
"""

# 导包
import pytest
import requests
from time import sleep
from api.template_api import TemplateAPI
from tools.get_log import GetLog
from tools.read_file import read_json
import allure

# 获取日志器
log = GetLog.get_log()


@allure.feature('测试类模板')
@pytest.skip("参考模板, 不执行")
class TestTemplate:
    session = None

    # 初始化方法
    @classmethod
    def setup_class(cls):
        cls.session = requests.Session()    # 初始化session对象
        cls.template = TemplateAPI()

    # 结束方法
    @classmethod
    def teardown_class(cls):
        cls.session.close()

    @classmethod
    def setup(cls):
        sleep(1.5)

    # 测试方法
    @allure.story("测试方法模板-add")
    @pytest.mark.parametrize(("attr1", "attr2", "success", "expect"), read_json("test_add"))
    def test_add(self, attr1, attr2, success, expect):
        # 添加功能API调用
        response = self.template.api_add(self.session, attr1, attr2)
        # 打印日志
        log.info("添加功能-状态码为: {}".format(response.status_code))
        # 断言状态码
        assert response.status_code == expect, "状态码断言失败"

    @allure.story("测试方法模板-upd")
    @pytest.mark.parametrize(("attr1", "attr2", "success", "expect"), read_json("test_upd"))
    def test_upd(self, attr1, attr2, success, expect):
        # 添加功能API调用
        response = self.template.api_upd(self.session, attr1, attr2)
        # 打印日志
        log.info("修改功能-状态码为: {}".format(response.status_code))
        # 断言状态码
        assert response.status_code == expect, "状态码断言失败"

    @allure.story("测试方法模板-get")
    @pytest.mark.parametrize(("attr1", "attr2", "success", "expect"), read_json("test_get"))
    def test_get(self, attr1, attr2, success, expect):
        # 添加功能API调用
        response = self.template.api_get(self.session, attr1, attr2)
        # 打印日志
        log.info("查询功能-状态码为: {}".format(response.status_code))
        # 断言状态码
        assert response.status_code == expect, "状态码断言失败"

    @allure.story("测试方法模板-del")
    @pytest.mark.parametrize(("uid", "success", "expect"), read_json("test_del"))
    def test_del(self, uid, success, expect):
        # 添加功能API调用
        response = self.template.api_del(self.session, uid)
        # 打印日志
        log.info("删除功能-状态码为: {}".format(response.status_code))
        # 断言状态码
        assert response.status_code == expect, "状态码断言失败"
