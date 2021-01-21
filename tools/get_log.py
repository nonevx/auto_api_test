# -*- coding:utf-8 -*-

"""
@File : get_log
@Author : Chen
@Contact : nonevxx@gmail.com
@Date : 2021/1/11 9:54
@Desc : 
"""

# 导包
import logging.handlers
import app


class GetLog:
    logger = None

    @classmethod
    def get_log(cls):
        if cls.logger is None:
            # 获取日志器
            cls.logger = logging.getLogger()
            # 设置级别
            cls.logger.setLevel(logging.INFO)
            # 获取处理器
            th = logging.handlers.TimedRotatingFileHandler(filename=app.BASE_DIR + "/log/log.log",
                                                           when="midnight",
                                                           interval=1,
                                                           backupCount=3,
                                                           encoding="utf-8")
            # 设置处理器级别
            th.setLevel(logging.INFO)
            # 获取格式器
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器
            th.setFormatter(fm)
            # 将处理器添加到日志器
            cls.logger.addHandler(th)
        # 返回日志器
        return cls.logger
