# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/11/27 21:18
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""


def get_module_names(module):
    return (i for i in dir(module) if i[0] == "M" and not "_" in i)


def get_all_names():
    from maya import (
        OpenMaya,
        OpenMayaAnim,
        OpenMayaFX,
        OpenMayaRender,
        OpenMayaUI,
        OpenMayaMPx,
    )
    names = [
        get_module_names(OpenMaya),
        get_module_names(OpenMayaAnim),
        get_module_names(OpenMayaFX),
        get_module_names(OpenMayaRender),
        get_module_names(OpenMayaUI),
        get_module_names(OpenMayaMPx),
    ]
    return (t for i in names for t in i)


def print_module_names(module):
    print("[{}]".format(
        ", \n".join(('"{}"'.format(i) for i in get_module_names(module)))
    ))


def print_all_names():
    print("[{}]".format(
        ", \n".join(('"{}"'.format(i) for i in get_all_names()))
    ))
