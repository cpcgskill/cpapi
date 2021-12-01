# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/1 9:22
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function
import os
import sys
from utils import init_maya, get_module_names, get_all_names

init_maya()
import maya.cmds as mc

version_str = str(mc.about(v=True))
import codecs
import json
from maya import (
    OpenMaya,
    OpenMayaAnim,
    OpenMayaFX,
    OpenMayaRender,
    OpenMayaUI,
    OpenMayaMPx,
)

modules = {"OpenMaya": OpenMaya, "OpenMayaAnim": OpenMayaAnim,
           "OpenMayaFX": OpenMayaFX, "OpenMayaRender": OpenMayaRender,
           "OpenMayaUI": OpenMayaUI, "OpenMayaMPx": OpenMayaMPx}
modules_data = {n: list(get_module_names(o)) for n, o in modules.items()}
if not os.path.isfile("./_maya_data.json"):
    with codecs.open("./_maya_data.json", "w", encoding="utf-8") as f:
        f.write("{}")
with codecs.open("./_maya_data.json", "r", encoding="utf-8") as f:
    data = json.loads(f.read())
    data[version_str] = {
        "modules_data": modules_data,
        "all": [i for i in modules_data.values() for t in i]
    }
with codecs.open("./_maya_data.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(data))
