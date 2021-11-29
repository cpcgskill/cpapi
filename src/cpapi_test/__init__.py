# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/11/29 8:06
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import os
import sys
import imp

os.environ["CPAPI_DEBUG"] = "on"
import cpapi

if not sys.modules.get("cpapi") is None:
    imp.reload(cpapi)

from cpapi_test import (utils, )

models = (utils,)
for m in models:
    imp.reload(m)


def test():
    for m in models:
        m.test()
