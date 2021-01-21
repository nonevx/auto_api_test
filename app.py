
# -*- coding:utf-8 -*-

"""
@File : app
@Author : Chen
@Contact : nonevxx@gmail.com
@Date : 2021/1/11 15:08
@Desc : 
"""

import os
import pytest


# 基础路由
BASE_URL = "http://localhost:5000"

# 获取脚本的绝对路径
ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)

pytest.main(["scripts/"])
