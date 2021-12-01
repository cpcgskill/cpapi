# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/1 9:13
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
import subprocess

path_template = r"C:\Program Files\Autodesk\{MAYA_VERSION}\bin\mayapy.exe"


def maya(version):
    return path_template.replace("{MAYA_VERSION}", version)


mayapy_paths = [
    maya("Maya2016"),
    maya("Maya2018"),
    maya("Maya2020"),
    maya("Maya2022"),
]
print(mayapy_paths)
root = os.path.abspath(os.curdir)
for p in mayapy_paths:
    c = '"{}" "{}"'.format(p, root + "/_class_name_utils.py")
    print(c)
    subprocess.Popen(c, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.read()

import codecs
import json

with codecs.open("./_maya_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

out_data = dict()
for k, v in data.items():
    for _k, _v in v["modules_data"].items():
        out_data[_k] = None
for k, v in data.items():
    for _k, _v in v["modules_data"].items():
        if out_data[_k] is None:
            out_data[_k] = set(_v)
        else:
            out_data[_k] = out_data[_k] & set(_v)
for k, v in out_data.items():
    out_data[k] = list(v)

all = []
for v in out_data.values():
    all += v
with codecs.open("./maya_data.json", "w", encoding="utf-8") as f:
    json.dump({
        "data": out_data,
        "all": all
    }, f)
