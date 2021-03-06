# coding = utf-8

'''
函数声明:
def name([arg,... arg = value,... *arg, **kwarg]):
    suite
1.
2. 当编译器遇到 def,会生成创建函数对象指令。
   也就是说 def 是执⾏行指令,⽽不仅仅是个语法关键字。
   可以在任何地⽅方动态创建函数对象。

lambda函数
不同于⽤用 def 定义复杂函数,lambda 只能是有返回值的简单的表达式。使⽤用赋值语句会引发语法 错误,可以考虑⽤用函数代替。

'''

'''
*****************************************************
1. 函数创建
   函数是第一类对象,可作为其他函数的实参或返回值。
   函数总是有返回值。就算没有 return,默认也会返回 None。
*****************************************************
'''
def test1(name):
    '''

    >>> test1('a').__name__
    'a'

    >>> test1('b').__name__
    'b'

    >>> test1('c').__name__
    'b'

    >>> test1('a')()
    call function a

    '''
    if name == "a":
        def a():
            print('call function a')
        return a
    else:
        def b(): pass
        return b

'''
*************************************************************
2. 参数
   2.1 函数的传参方式灵活多变,可按位置顺序传参,也可不关⼼顺序⽤命名实参。
*************************************************************
'''
def test21(a, b):
    '''

    >>> test2(1,2)      # 位置参数
    1 2

    >>> test2(b=3,a=4)  # 命名参数
    4 3
    '''
    print(a, b)

'''
*************************************************************
   2.2 ⽀持参数默认值。不过要⼩⼼,
       默认值对象在创建函数时生成,所有调用都使⽤同⼀对象。
       如果该默认值是可变类型,那么就如同 C 静态局部变量。
*************************************************************
'''
def test22(x, lst=[]):
    '''
    >>> test22(1)
    [1]

    >>> test22(2)   # 保持了上次调⽤用状态。
    [1, 2]

    >>> test22(3, [])   # 显式提供实参,不使⽤用默认值。
    [3]

    >>> test22(3)   # 再次使⽤用默认值,会继续使用默认的列表对象
    [1, 2, 3]

    '''

    lst.append(x)
    return lst

'''
*************************************************************
   2.3 默认参数后⾯不能有其他位置参数,除非是变参。
   SyntaxError: def test23(a, b=1, c): pass

   2.4 用 *args 收集 "多余" 的位置参数,**kwargs 收集 "额外" 的命名参数。
       这两个名字只是惯例,可 ⾃自由命名。
*************************************************************
'''
def test24(a, b=1, *args, **kwargs):
    '''

    >>> test24(0)
    0
    1
    ()
    {}

    >>> test24(0,2,3,4)
    0
    2
    (3, 4)
    {}

    >>> test24(0,2,3,4,x=5)
    0
    2
    (3, 4)
    {'x': 5}

    # 可 "展开" 序列类型和字典,将全部元素当做多个实参使⽤用。如不展开的话,那仅是单个实参对象。
    >>> test24(*range(5), **{'x': 10, 'y': 11})
    0
    1
    (2, 3, 4)
    {'x': 10, 'y': 11}

    >>> test24(range(5))
    range(0, 5)
    1
    ()
    {}

    # 单个 "*" 展开序列类型,或者仅是字典的主键列表。
    # "**" 展开字典键值对。但如果没有变参收集, 展开后多余的参数将引发异常。
    >>> p = dict(a=20,b=21)

    >>> test24(p)
    {'a': 20, 'b': 21}
    1
    ()
    {}

    >>> test24(*p)  # 仅展开 keys(),test("a"、"b")
    a
    b
    ()
    {}

    >>> test24(**p)  # 展开 items(),test(a = 1, b = 2)。
    20
    21
    ()
    {}
    '''

    print(a)
    print(b)
    print(args)
    print(kwargs)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)