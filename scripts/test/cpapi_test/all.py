# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/11/29 22:27
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function


def test_array():
    import cpapi.all as api
    print("test float array>> ", [i for i in api.MFloatArray(10, 0)])


def test_iter():
    import cpapi.all as api
    itdg = api.MItDependencyNodes()
    print("test itdg>> ", [itdg.thisNode() for _ in itdg])


def test():
    test_array()
    test_iter()
