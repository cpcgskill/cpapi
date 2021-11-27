#!/usr/bin/python
# -*-coding:utf-8 -*-
u"""
:创建时间: 2020/5/18 23:57
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

* 本模块提供了对Maya Api数组的封装让其可以顺利的融入Python循环机制中
    >>> import cpapi as api
    >>> api.OpenMaya.MFloatArray(10, 0)
    <class 'CPMel.api.__OpenMaya_array__.MFloatArray'>[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    >>> arr = api.OpenMaya.MFloatArray(10, 0)
    >>> [i for i in arr]
    [<CPMel.api.__OpenMaya_it__.MItDag; proxy of <Swig Object of type 'MItDag *' at 0x0000000016A16E10> >,...]

* 不仅如此还提供了迭代器的封装
    >>> from cpapi.OpenMaya import MItDag
    >>> itdg = MItDag()
    >>> [i for i in itdg] # 注意迭代器循环的 “i”是迭代器本身


"""
# 初始化MayaApi
# 如果不在此处初始化会导致未知的错误
import cpapi.init_imp

from cpapi import (
    __OpenMaya__,
    __OpenMayaAnim__,
    __OpenMayaRender__,
    __OpenMayaFX__,
    __OpenMayaUI__,
    __OpenMayaMPx__,
)

from cpapi import (
    __OpenMaya_it__,
    __OpenMayaAnim_it__
)

from cpapi import (
    __OpenMaya_array__,
    __OpenMayaAnim_array__
)

from cpapi import (
    OpenMaya,
    OpenMayaAnim,
    OpenMayaFX,
    OpenMayaRender,
    OpenMayaUI,
    OpenMayaMPx,
)
from cpapi import iter

DEBUG = True
if DEBUG:
    from imp import reload

    reload(__OpenMaya__)
    reload(__OpenMayaAnim__)
    reload(__OpenMayaFX__)
    reload(__OpenMayaRender__)
    reload(__OpenMayaUI__)
    reload(__OpenMayaMPx__)
    reload(__OpenMaya_it__)
    reload(__OpenMayaAnim_it__)
    reload(__OpenMaya_array__)
    reload(__OpenMayaAnim_array__)
    reload(OpenMaya)
    reload(OpenMayaAnim)
    reload(OpenMayaFX)
    reload(OpenMayaRender)
    reload(OpenMayaUI)
    reload(OpenMayaMPx)
    reload(iter)

__all__ = [
    "OpenMaya",
    "OpenMayaAnim",
    "OpenMayaFX",
    "OpenMayaRender",
    "OpenMayaUI",
    "OpenMayaMPx",
    "iter"
]
