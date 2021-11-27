# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/11/19 8:51
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import functools
from .all import MObject, MSelectionList, MGlobal, \
    MItDependencyNodes, MItDag, MItSelectionList, \
    MFnDependencyNode, MFnDagNode, MFn


class NodeGen(object):
    def __init__(self, it):
        self.it = (i for i in it)

    def to_list(self, key=None):
        if key is None:
            return [i for i in self.node_objects()]
        else:
            return [key(i) for i in self.node_objects()]

    def node_objects(self):
        return (i for i in self.it)

    def mfn(self):
        return (MFnDependencyNode(i) for i in self.node_objects())

    def filter(self, key):
        return NodeGen((i for i in self.node_objects() if key(i)))

    def filter_type(self, t_name):
        return self.filter(key=lambda i: MFnDependencyNode(i).typeName() == t_name)


def node_gen(fn):
    @functools.wraps(fn)
    def _(*args, **kwargs):
        return NodeGen(fn())

    return _


def _re_decorator(key):
    def _wrapper(fn):
        @functools.wraps(fn)
        def _(*args, **kwargs):
            return (key(i) for i in fn(*args, **kwargs))

        return _

    return _wrapper


def _filter_decorator(key):
    def _wrapper(fn):
        @functools.wraps(fn)
        def _(*args, **kwargs):
            return (i for i in fn(*args, **kwargs) if key(i))

        return _

    return _wrapper


def _mfn_from_objects(mfn):
    return _re_decorator(key=lambda i: mfn(i))


_filter_empty_objects = _filter_decorator(key=lambda i: not i.isNull())


@_mfn_from_objects(MFnDependencyNode)
@_filter_empty_objects
def iter_node():
    it = MItDependencyNodes(MFn.kDependencyNode)
    while not it.isDone():
        yield it.thisNode()
        it.next()


@_mfn_from_objects(MFnDagNode)
@_filter_empty_objects
def iter_dag_node():
    it = MItDag()
    while not it.isDone():
        yield it.currentItem()
        it.next()


@_mfn_from_objects(MFnDependencyNode)
@_filter_empty_objects
def selected_node():
    sel = MSelectionList()
    MGlobal.getActiveSelectionList(sel)
    it = MItSelectionList(sel, MFn.kDependencyNode)
    while not it.isDone():
        obj = MObject()
        it.getDependNode(obj)
        yield obj
        it.next()
