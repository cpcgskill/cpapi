# cpapi

OpenMaya api 封装

## 快速开始
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

## 功能介绍

#### 本模块提供了对Maya Api数组的封装让其可以顺利的融入Python循环机制中

```python
import cpapi.OpenMaya as om

[i for i in om.MFloatArray(10, 0)]
```
```
[<cpapi.__OpenMaya_it__.MItDag; proxy of <Swig Object of type 'MItDag *' at 0x0000000016A16E10> >,...]
```


#### 不仅如此还提供了迭代器的封装

```python
import cpapi.OpenMaya as om

itdg = om.MItDag()
[i for i in itdg]  # 注意迭代器循环的 “i”是迭代器itdg本身
```

### 工具集模块
```python
import cpapi.all as api
import cpapi.utils as cputils
print("test selected>> ", cputils.selected())
o = api.MFnDependencyNode().create("joint", "joint1")
p = cputils.mobject_to_mdagpath(o)
print("test mobject_to_mdagpath>> ", p)
print("test mdagpath_to_mobject>> ", cputils.mdagpath_to_mobject(p))
```
```
test selected>>  []
test mobject_to_mdagpath>>  <maya.OpenMaya.MDagPath; proxy of <Swig Object of type 'MDagPath *' at 0x000001CE99D49480> >
test mdagpath_to_mobject>>  MObject<0x1ce9abf0128L>
```

