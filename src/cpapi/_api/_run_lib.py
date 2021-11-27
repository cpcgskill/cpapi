# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/11/28 0:30
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function


def base(cls):
    cls.__str__ = lambda self: "{}<{}>".format(self.__class__.__name__, hex(id(self)))
    cls.__repr__ = lambda self: self.__str__()
    return cls
