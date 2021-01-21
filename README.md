# auto_api_test


> 开发环境: Pycharm
>
> 开发语言&版本:  python3.7.8
>
> 测试框架: Pytest、测试报告: Allure
>
> 版本管理: Git

## 项目目录结构

- api	-- 模仿PO模式, 抽象出页面类, 页面类内包含页面所包含所有接口, 并封装成方法可供其他模块直接调用
- config    -- 配置文件目录
- data    -- 测试数据目录
- doc    -- 文档存放目录
- log    -- 日志
- report    -- 测试报告
- scripts    -- 测试脚本存放目录
- tools    -- 工具类目录
- .gitignore    -- git忽略
- app.py    -- 命令行启动入口
- pytest.ini    -- pytest测试框架配置文件
- README.md    -- 开发说明文档

## 代码分析

**pytest.ini**

> pytest框架的配置文件

```python
[pytest]
addopts = --html=../report/report.html    # pytest-html报告插件配置 
;addopts = -s --alluredir report    # allure-pytest报告插件配置
testpaths = ./scripts    # 设置用例目录识别名称
python_files = test*_*.py    # 设置测试文件识别名称
python_classes = Test*    # 设置测试类识别名称
python_functions = test_*    # 设置测试方法识别名称
```

**app.py**

> 

```python
# 基础路由(方便在部署环境发生变化时切换全局基础路由)
BASE_URL = "http://xxxx.com"
# 获取脚本的绝对路径(脚本在项目根目录就可以理解为项目路径)
ABS_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(ABS_PATH)

# 命令行启动此脚本时执行测试用例
pytest.main(["scripts/"])
```

**/config/config.json**

> 配置文件, 目前包含全局请求头配置、类似全局变量的设置, 可通过tools内的工具函数进行读写
> 请求头具体参数根据需要自行配置

```json
{
  "headers": {
    "Host": "xxx.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "Authorization": "xxxx",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "http://xxx.com",
    "Referer": "http://xxx.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9"
  }
}
```

**/api/template_api.py**

> 页面类模板, 包含页面接口的请求方法(增删改查)封装, 主要在此定义好接口和请求入参等内容

```python
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

```

**/scripts/test_template.py**

> 测试类以Test开头, 测试类和测试方法添加allure装饰器
>
> 前置测试类方法 - 初始化requests请求库的session对象, 创建对应的页面对象
>
> 后置测试类方法 - 关闭session对象
>
> 前置测试方法 - 加休眠
>
> 测试方法中添加可选参数化装饰器, 测试方法中通过页面对象调用页面接口请求方法, 传入requests的session对象和方法需要的必要参数, 进行响应结果的处理和断言等操作
>
> 日志器可通过引入工具调用

```python
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

```

**/data  | /tools**

> 测试数据和具体的操作工具类根据需要自定义
