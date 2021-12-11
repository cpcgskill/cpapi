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
    print("test mobject_to_mdagpath>> ", cputils.mobject_to_mdagpath(o))
    print("test mobject_to_muuid>> ", cputils.mobject_to_muuid(o))
    p = cputils.mobject_to_mdagpath(o)

    print("test mdagpath_to_mobject>> ", cputils.mdagpath_to_mobject(p))
    print("test mdagpath_to_muuid>> ", cputils.mdagpath_to_muuid(p))
    uid = cputils.mdagpath_to_muuid(p)

    print("test muuid_to_mdagpath>> ", cputils.muuid_to_mdagpath(uid))
    print("test muuid_to_mobject>> ", cputils.muuid_to_mobject(uid))

    print("test name_to_mobject>> ", cputils.name_to_mobject("joint1"))
    print("test name_to_mdagpath>> ", cputils.name_to_mdagpath("joint1"))
    print("test name_to_components>> ", cputils.name_to_components("joint1"))
    print("test name_to_components_mobject>> ", cputils.name_to_components_mobject("joint1"))
    print("test name_to_muuid>> ", cputils.name_to_muuid("joint1"))

    print("test active_selectionlist>> ", cputils.active_selectionlist())
    print("test selected>> ", cputils.selected())
