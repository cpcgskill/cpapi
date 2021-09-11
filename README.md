# cpapi

OpenMaya api 包装

* 本模块提供了对Maya Api数组的封装让其可以顺利的融入Python循环机制中
  > [i for i in cpapi.OpenMaya.MFloatArray(10, 0)]
  >
  [<cpapi.__OpenMaya_it__.MItDag; proxy of <Swig Object of type 'MItDag *' at 0x0000000016A16E10> >,...]


* 不仅如此还提供了迭代器的封装
  > itdg = cpapi.OpenMaya.MItDag()
  >
  [i for i in itdg] # 注意迭代器循环的 “i”是迭代器本身