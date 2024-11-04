#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright DataGrand Tech Inc. All Rights Reserved.
Author: Prince
File: log.py
Time: 2023-01-28 12:03
"""
import os
import re
import sys
import logging

from loguru import logger


class InterceptHandler(logging.Handler):
    """
    删除日志颜色

    不同框架底层方法在写入日志时,有可能被loguru判断为带颜色的日志从而进入后续处理,导致写入错误.
    请务必保留此方法,避免日志写入导致错误.
    """
    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info, colors=False)
        ansi_escape = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")  # 删除自带的颜色
        logger_opt.log(record.levelname, ansi_escape.sub("", record.getMessage()))


def register_logger():
    """注册日志到loguru，由loguru统一管理日志的格式、旋转、错误等"""
    # [定义日志路径]
    os.makedirs("./log", exist_ok=True)

    # [标准日志写入loguru] 此配置可将各库写入原生logging的日志配置入loguru,例如Flask
    logging.basicConfig(handlers=[InterceptHandler(level="INFO")], level="INFO")

    # [loguru日志输出至控制台] 对调试有帮助
    logger.configure(handlers=[{"sink": sys.stderr, "level": "INFO"}])

    # 日志旋转、大小限制、更替等参数均支持多种配置,详情请参考文档
    # [logger参数文档: https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger]
    # 请务必设置colorize=False,避免在不同系统上由于颜色标签的写入造成问题
    cus_format = "{time:%Y-%m-%d %H:%M:%S} | {level}  | {process} | {thread} | {name}:{function}:{line} - {message}"
    logger.add("./log/info_{time:%Y-%m-%d}.log", level="INFO", format=cus_format, colorize=False, rotation="1 days", retention="7 days",
               backtrace=False, diagnose=False, encoding="utf-8")
    logger.add("./log/error_{time:%Y-%m-%d}.log", level="ERROR", format=cus_format, colorize=False, rotation="1 days", retention="15 days",
               backtrace=False, diagnose=False, encoding="utf-8")
    logger.add("./log/error_detail_{time:%Y-%m-%d}.log", level="ERROR", format=cus_format, colorize=False, rotation="1 days",
               retention="3 days", backtrace=True, diagnose=True,  encoding="utf-8")