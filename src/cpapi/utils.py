# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/11/29 8:01
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from .all import *
from . import iter


def mobject_to_mdagpath(o):
    """
    :type o: MObject
    :rtype: MDagPath
    """
    return MDagPath.getAPathTo(o)


def mdagpath_to_mobject(p):
    """

    :type p: MDagPath
    :rtype: MObject
    """
    sel = MSelectionList()
    sel.add(p)
    o = MObject()
    sel.getDependNode(0, o)
    return o


def selected():
    return list(iter.selected())
