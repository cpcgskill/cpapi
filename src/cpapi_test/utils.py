# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/11/29 8:05
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function


def test():
    import cpapi.all as api
    import cpapi.utils as cputils
    print("test selected>> ", cputils.selected())
    o = api.MFnDependencyNode().create("joint", "joint1")
    p = cputils.mobject_to_mdagpath(o)
    print("test mobject_to_mdagpath>> ", p)
    print("test mdagpath_to_mobject>> ", cputils.mdagpath_to_mobject(p))
