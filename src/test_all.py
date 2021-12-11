# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/11 14:35
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function

try:
    import maya.standalone

    maya.standalone.initialize(name='python')
except:
    pass
import os
import imp
import maya.cmds as mc
os.environ["CPAPI_DEBUG"] = "on"

import cpapi

imp.reload(cpapi)

import cpapi_test
cpapi_test.test()