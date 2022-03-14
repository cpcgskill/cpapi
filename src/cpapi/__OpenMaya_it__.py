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
from . import __OpenMaya__ as om
from .__ALL import rebuild_maya_iter


# MItCurveCV, MItDag, MItDependencyGraph, MItDependencyNodes, MItEdits, MItGeometry, MItInstancer, MItMeshEdge, MItMeshFaceVertex, MItMeshPolygon, MItMeshVertex, MItSelectionList, MItSubdEdge, MItSubdFace, MItSubdVertex, MItSurfaceCV, MIteratorType

class MItCurveCV(om.MItCurveCV):
    def __iter__(self):
        return rebuild_maya_iter(self)


class MItDag(om.MItDag):
    def __iter__(self):
        return rebuild_maya_iter(self)


class MItDependencyGraph(om.MItDependencyGraph):
    def __iter__(self):
        return rebuild_maya_iter(self)


class MItDependencyNodes(om.MItDependencyNodes):
    def __iter__(self):
        return rebuild_maya_iter(self)


class MItEdits(om.MItEdits):
    def __iter__(self):
        return rebuild_maya_iter(self)


class MItGeometry(om.MItGeometry):
    def __iter__(self):
        return rebuild_maya_iter(self)


class MItInstancer(om.MItInstancer):
    def __iter__(self):
        return rebuild_maya_iter(self)


class MItMeshEdge(om.MItMeshEdge):
    def __iter__(self):
        return rebuild_maya_iter(self)


class MItMeshFaceVertex(om.MItMeshFaceVertex):
    def __iter__(self):
        return rebuild_maya_iter(self)


class MItMeshPolygon(om.MItMeshPolygon):
    def __iter__(self):
        return rebuild_maya_iter(self)


class MItMeshVertex(om.MItMeshVertex):
    def __iter__(self):
        return rebuild_maya_iter(self)


class MItSelectionList(om.MItSelectionList):
    def __iter__(self):
        return rebuild_maya_iter(self)


class MItSubdEdge(om.MItSubdEdge):
    def __iter__(self):
        return rebuild_maya_iter(self)


class MItSubdFace(om.MItSubdFace):
    def __iter__(self):
        return rebuild_maya_iter(self)


class MItSubdVertex(om.MItSubdVertex):
    def __iter__(self):
        return rebuild_maya_iter(self)


class MItSurfaceCV(om.MItSurfaceCV):
    def __iter__(self):
        return rebuild_maya_iter(self)


class MIteratorType(om.MIteratorType):
    def __iter__(self):
        return rebuild_maya_iter(self)


__all__ = ["MItCurveCV", "MItDag", "MItDependencyGraph", "MItDependencyNodes", "MItEdits", "MItGeometry",
           "MItInstancer", "MItMeshEdge", "MItMeshFaceVertex", "MItMeshPolygon", "MItMeshVertex", "MItSelectionList",
           "MItSubdEdge", "MItSubdFace", "MItSubdVertex", "MItSurfaceCV", "MIteratorType"]
