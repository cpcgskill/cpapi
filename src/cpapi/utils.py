# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/11/29 8:01
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
工具集模块
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


def _name_to_mselectionlist(n):
    """
    :type n: str|unicode
    :rtype: MSelectionList
    """
    sel = MSelectionList()
    sel.add(n)
    return sel


def _mselectionlist_to_mobject(sel):
    """
    :type sel: MSelectionList
    :rtype: MObject
    """
    o = MObject()
    sel.getDependNode(0, o)
    return o


def _mselectionlist_to_mdagpath(sel):
    """
    :type sel: MSelectionList
    :rtype: MDagPath
    """
    p = MDagPath()
    sel.getDagPath(0, p)
    return p


def name_to_mobject(n):
    """
    :type n: str|unicode
    :rtype: MObject
    """
    return _mselectionlist_to_mobject(_name_to_mselectionlist(n))


def _mselectionlist_to_components_mobject(sel):
    """

    :type sel: MSelectionList
    :return: MObject
    """
    obj = MObject()
    sel.getDagPath(0, MDagPath(), obj)
    return obj


def name_to_mdagpath(n):
    """
    :type n: str|unicode
    :rtype: MDagPath
    """
    return _mselectionlist_to_mdagpath(_name_to_mselectionlist(n))


def name_to_components_mobject(n):
    """
    :type n: str|unicode
    :return: MObject
    """
    return _mselectionlist_to_components_mobject(_name_to_mselectionlist(n))


def active_selectionlist():
    """
    获得当前活动选择列表
    :rtype: MSelectionList
    """
    sel = MSelectionList()
    MGlobal.getActiveSelectionList(sel)
    return sel


def selected():
    """
    获得当前选择节点的MObject
    :rtype:list[MObject]
    """
    return list(iter.selected())
