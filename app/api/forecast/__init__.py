#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author  : MG
@Time    : 2018/3/30 17:43
@File    : __init__.py.py
@contact : mmmaaaggg@163.com
@desc    : 
"""
from flask_restplus import Namespace
import logging
logger = logging.getLogger(__name__)
# __name__.split('.')[-1] 相当于 asset 文件名
# 目标文件默认使用 templates/asset 下的文件
# file_name = __name__.split('.')[-1]
logger.info('import %s', __name__)
api = Namespace('forecast', description='预测')

from .views import *
