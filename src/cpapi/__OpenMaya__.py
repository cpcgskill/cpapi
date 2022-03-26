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
"""
from __future__ import unicode_literals, print_function
from ._api import OpenMaya
from ._api.OpenMaya import *

ScriptUtil = OpenMaya.MScriptUtil()


class MObject(OpenMaya.MObject):
    def __str__(self):
        if self.isNull():
            return "MObject(null)"
        else:
            return 'MObject(not null, type={})'.format(self.apiTypeStr())


class MDagPath(OpenMaya.MDagPath):
    def __str__(self):
        return 'MDagPath("{}")'.format(self.fullPathName())


class MSelectionList(OpenMaya.MSelectionList):
    def __str__(self):
        names = []
        self.getSelectionStrings(names)
        return 'MSelectionList({})'.format(names)


class MMatrix(OpenMaya.MMatrix):
    def __str__(self):
        return "Matrix%s" % str(tuple([[self(i, t) for t in range(4)] for i in range(4)]))

    def __repr__(self):
        return self.__str__()

    # def __getitem__(self, item):
    #     if isinstance(item, int):
    #         return (self(item, 0), self(item, 1), self(item, 2), self(item, 3))
    #     else:
    #         return self(*item)


class MPoint(OpenMaya.MPoint, object):

    def __str__(self):
        return "MPoint%s" % str((self.x, self.y, self.z))

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, OpenMaya.MPoint):
            other = OpenMaya.MVector(other)
        return OpenMaya.MPoint.__add__(self, other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
        yield self.w


class MFloatPoint(OpenMaya.MFloatPoint):
    def __str__(self):
        return "MFloatPoint%s" % str((self.x, self.y, self.z))

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, OpenMaya.MFloatPoint):
            other = OpenMaya.MFloatVector(other)
        return OpenMaya.MFloatPoint.__add__(self, other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
        yield self.w


class MVector(OpenMaya.MVector):
    def __str__(self):
        return "MVector%s" % str((self.x, self.y, self.z))

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z


class MFloatVector(OpenMaya.MFloatVector):
    def __str__(self):
        return "MFloatVector%s" % str((self.x, self.y, self.z))

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
