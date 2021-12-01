# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/11/28 4:58
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function
from utils import *


def print_OpenMaya_code(module, header="# -*-coding:utf-8 -*-"):
    names = list(get_module_names(module))
    imp_lib = "from ._run_lib import *"
    from_imp = "import {} as orig".format(module.__name__)
    body = "\n".join("@base\nclass {}(orig.{}):pass".format(i, i) for i in names)
    from_imp_all_var = "__all__ = {}".format(repr(names))
    print("\n".join([header, imp_lib, from_imp, body, from_imp_all_var]))

root = r"D:\Development\python_maya\cpapi\src\cpapi\_api"
import sys



import codecs
import json
with codecs.open("./maya_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)
for k,v in data["data"].items():
    with codecs.open("{}/{}.py".format(root, k), "w", encoding="utf-8") as f:
        header = "# -*-coding:utf-8 -*-"
        names = v
        imp_lib = "from ._run_lib import *"
        from_imp = "import maya.{} as orig".format(k)
        body = "\n".join("@base\nclass {}(orig.{}):pass".format(i, i) for i in names)
        from_imp_all_var = "__all__ = {}".format(repr(names))
        f.write("\n".join([header, imp_lib, from_imp, body, from_imp_all_var]))