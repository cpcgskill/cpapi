# cpapi

OpenMaya api 封装

## 目录

- [快速开始](#快速开始)
- [功能介绍](#功能介绍)
    - [MayaApi数组的封装](#MayaApi数组的封装)
    - [迭代器的封装](#迭代器的封装)
    - [工具集模块](#工具集模块)
- [版权说明](#版权说明)

### 快速开始

1. 打开C:\Users\PC\Documents\maya文件夹
2. 进入scripts文件夹，如果没有就创建它
3. 下载完整的cpapi代码
4. 解压并进入解压完成的文件夹
5. 将src目录中的cpapi文件夹复制到scripts
6. 打开maya2018，如果已经打开了就重启它
7. 打开脚本编辑器并执行以下示例代码

```python
from __future__ import unicode_literals, print_function
from cpapi.all import MItDependencyNodes, MGlobal

MGlobal.displayWarning("场景节点有： {}".format([i.thisNode() for i in MItDependencyNodes()]))
```

### 功能介绍

#### MayaApi数组的封装

本模块提供了对MayaApi数组的封装让其可以顺利的融入Python循环机制中

```python
from __future__ import unicode_literals, print_function


def test_array():
    import cpapi.all as api
    print("test float array>> ", [i for i in api.MFloatArray(10, 0)])


test_array()
```

```
test float array>>  [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```

#### 迭代器的封装

不仅如此还提供了迭代器的封装

```python
from __future__ import unicode_literals, print_function


def test_iter():
    import cpapi.all as api
    itdg = api.MItDependencyNodes()
    print("test itdg>> ", [itdg.thisNode() for _ in itdg])


test_iter()
```

```
test itdg>>  [<maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE990A4990> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE990A4B10> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE990A4B70> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9ABD8420> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9ABD8870> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9ABD8C60> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9ABD8060> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A4E7420> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE99D49450> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79D060> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79D600> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79D660> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79D6F0> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79D780> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79D810> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79D8A0> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79D8D0> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79D900> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79D930> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79D960> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79D990> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79D9C0> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79D9F0> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DA20> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DA50> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DA80> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DAB0> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DAE0> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DB10> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DB40> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DB70> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DBA0> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DBD0> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DC00> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DC30> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DC60> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DC90> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DCC0> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DCF0> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DD20> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DD50> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DD80> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DDB0> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DDE0> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DE10> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DE40> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DE70> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DEA0> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DED0> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DF00> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DF30> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DF60> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DF90> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A79DFC0> >, <maya.OpenMaya.MObject; proxy of <Swig Object of type 'MObject *' at 0x000001CE9A57D030> >]
```

#### 迭代器模块

```python
from __future__ import unicode_literals, print_function


def test():
    import cpapi.iter as cpit
    print("test iter_node>> ", cpit.iter_node())
    print("test iter_dag_node>> ", cpit.iter_dag_node())
    print("test selected_node>> ", cpit.selected_node())
    print("test selected>> ", cpit.selected())


test()
```

```
test iter_node>>  <generator object <genexpr> at 0x000001CE9AFD2360>
test iter_dag_node>>  <generator object <genexpr> at 0x000001CE9A780678>
test selected_node>>  <generator object <genexpr> at 0x000001CE9AFD23A8>
test selected>>  <generator object <genexpr> at 0x000001CE9AFD23A8>
```

#### 工具集模块

```python
from __future__ import unicode_literals, print_function


def test():
    import cpapi.all as api
    import cpapi.utils as cputils
    print("test selected>> ", cputils.selected())
    o = api.MFnDependencyNode().create("joint", "joint1")
    p = cputils.mobject_to_mdagpath(o)
    print("test mobject_to_mdagpath>> ", p)
    print("test mdagpath_to_mobject>> ", cputils.mdagpath_to_mobject(p))
    print("test name_to_mobject>> ", cputils.name_to_mobject("joint1"))
    print("test name_to_mdagpath>> ", cputils.name_to_mdagpath("joint1"))
    print("test name_to_components>> ", cputils.name_to_components("joint1"))
    print("test name_to_components_mobject>> ", cputils.name_to_components_mobject("joint1"))
    print("test active_selectionlist>> ", cputils.active_selectionlist())


test()
```

```
test selected>>  []
test mobject_to_mdagpath>>  MDagPath("|joint1")
test mdagpath_to_mobject>>  MObject(not null, type=kJoint)
test name_to_mobject>>  MObject(not null, type=kJoint)
test name_to_mdagpath>>  MDagPath("|joint1")
test name_to_components>>  (MDagPath("|joint1"), MObject(null))
test name_to_components_mobject>>  MDagPath("|joint1")
test active_selectionlist>>  MSelectionList([])
```

### 版权说明

该项目签署了Apache-2.0 授权许可，详情请参阅 LICENSE