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


def _name_to_mselectionlist(n):
    """
    :type n: str|unicode
    :rtype: MSelectionList
    """
    sel = MSelectionList()
    sel.add(n)
    return sel


def _mdagpath_to_mselectionlist(p):
    """

    :type p: MDagPath
    :rtype: MSelectionList
    """
    sel = MSelectionList()
    sel.add(p)
    return sel


def _muuid_to_mselectionlist(uid):
    """

    :type uid: MUuid
    :rtype: MSelectionList
    """
    sel = MSelectionList()
    sel.add(uid)
    return sel


def _mobject_to_mselectionlist(o):
    """

    :type p: MObject
    :rtype: MSelectionList
    """
    sel = MSelectionList()
    sel.add(o)
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


def _mselectionlist_to_components(sel):
    """

    :type sel: MSelectionList
    :rtype: (MDagPath, MObject)
    """
    p = MDagPath()
    o = MObject()
    sel.getDagPath(0, p, o)
    return (p, o)


def _mselectionlist_to_components_mobject(sel):
    """

    :type sel: MSelectionList
    :rtype: MObject
    """
    return _mselectionlist_to_components(sel)[0]


def _mselectionlist_to_muuid(sel):
    """

    :type sel: MSelectionList
    :rtype: MUuid
    """
    o = MObject()
    sel.getDependNode(0, o)
    return MFnDependencyNode(o).uuid()


def mobject_to_mdagpath(o):
    """
    :type o: MObject
    :rtype: MDagPath
    """
    return MDagPath(MDagPath.getAPathTo(o))


def mobject_to_muuid(o):
    """
    :type o: MObject
    :rtype: MUuid
    """
    return _mselectionlist_to_muuid(_mobject_to_mselectionlist(o))


def mdagpath_to_mobject(p):
    """

    :type p: MDagPath
    :rtype: MObject
    """
    return _mselectionlist_to_mobject(_mdagpath_to_mselectionlist(p))


def mdagpath_to_muuid(p):
    """

    :type p: MDagPath
    :rtype: MUuid
    """
    return _mselectionlist_to_muuid(_mdagpath_to_mselectionlist(p))


def muuid_to_mdagpath(uid):
    return mobject_to_mdagpath(_mselectionlist_to_mobject(_muuid_to_mselectionlist(uid)))


def muuid_to_mobject(uid):
    return _mselectionlist_to_mobject(_muuid_to_mselectionlist(uid))



def name_to_mobject(n):
    """
    :type n: str|unicode
    :rtype: MObject
    """
    return _mselectionlist_to_mobject(_name_to_mselectionlist(n))


def name_to_mdagpath(n):
    """
    :type n: str|unicode
    :rtype: MDagPath
    """
    return _mselectionlist_to_mdagpath(_name_to_mselectionlist(n))


def name_to_components(n):
    """
    :type n: str|unicode
    :rtype: (MDagPath, MObject)
    """
    return _mselectionlist_to_components(_name_to_mselectionlist(n))


def name_to_components_mobject(n):
    """
    :type n: str|unicode
    :rtype: MObject
    """
    return _mselectionlist_to_components_mobject(_name_to_mselectionlist(n))


def name_to_muuid(n):
    """
    :type n: str|unicode
    :rtype: MUuid
    """
    return _mselectionlist_to_muuid(_name_to_mselectionlist(n))


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

    def _():
        sel = active_selectionlist()
        it = MItSelectionList(sel)
        while not it.isDone():
            if it.itemType() == MItSelectionList.kDNselectionItem:
                obj = MObject()
                it.getDependNode(obj)
                yield obj
            it.next()

    return list(_())
