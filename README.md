# PythonLearningNotes
本文采用Python doctest单元测试的方法，直接用代码学习代码，滚雪球式的迭代学习。

doctest是一个python标准库自带的轻量单元测试工具，适合实现一些简单的单元测试。它可以在docstring中寻找测试用例并执行，比较输出结果与期望值是否符合。

运行命令

> python -m doctest -v dtest.py 

如果doctest通过，不会有任何输出。可以加-v参数来查看测试细节。

 关于doctest的简单使用请参考：http://mickhan.blog.51cto.com/2517040/944294
