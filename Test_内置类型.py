# coding=utf-8
import unittest
from decimal import *

'''
Python中的一切都是对象
Python的"变量" 更准确的词语可以叫"名字"或"标签"

数据类型：
空值：None
数字：bool, int, float, complex
序列：str, list, tuple
字典：dict
集合：set, frozenset
'''

class TestDataType(unittest.TestCase):

    def test_bool(self):
        listFalse = map(bool,[None, 0, '', u'', list(), tuple(),dict(), set(), frozenset()])   # map是一个高阶函数
        l = list(listFalse)
        self.assertEqual(l, [False, False, False, False, False, False, False, False, False])
        self.assertEqual(l, [False] * 9)

        # True, False可以当作数字使用，有点奇怪
        print('True: ', int(True), '; False:', int(False))

        a = 'abcd'
        i = 8
        self.assertEqual(a[False], 'a')
        self.assertEqual(a[True], 'b')

        self.assertEqual(a[i>9], 'a')
        self.assertEqual(a[i>6], 'b')


    def test_int(self):
        # 小数字和大数字的区别 -5,257
        x = 25
        y = 25
        self.assertEqual(x is y, True)

        x = 2**8
        y = 2**8
        self.assertEqual(x is y, True)

        x = 2**8 + 1
        y = 2**8 + 1
        self.assertEqual(x is y, False)

        x = 257
        y = 257
        self.assertEqual(x is y, True)   #  ???


    def test_float(self):
        self.assertEqual(3/2, 1.5)
        self.assertEqual(3 // 2, 1)

        self.assertEqual(3*0.1 == 0.3, False)       # 浮点数不要直接比较是否相等，如果需要使用Decimal库
        self.assertEqual(3 * Decimal('0.1') == Decimal('0.3'), True)

        self.assertEqual(round(2.675,2), 2.67)      # 没有四舍五入

    def test_str(self):
        self.assertEqual("a"'b'"c", 'abc')  # 自动合并多个相邻字符串
        self.assertEqual(len('abcd'), 4, 'error: string length')    # 字符串长度

        self.assertEqual('a' + 'b', "ab")
        self.assertEqual('ab' * 3, "ababab") # 复制字符串
        self.assertEqual("-".join(['a','b','c']), "a-b-c")  # 用指定字符合并多个字符串
        self.assertEqual("a-b-c".split('-'), ['a','b','c']) # 用指定字符分割字符串

        names = 'jack\nrose\ntom'
        lstNames = ['jack','rose','tom']
        self.assertEqual(names.split('\n'), lstNames)
        self.assertEqual(names.splitlines(), lstNames)  # 按行分割

        a = '<body>'
        self.assertEqual(a.startswith('<'), True)
        self.assertEqual(a.endswith('>'), True)

        self.assertEqual('aBcD'.upper(), 'ABCD')    # 大些转换
        self.assertEqual('aBcD'.lower(), 'abcd')    # 小些转换

        self.assertEqual('_abcabc_'.find("bc"), 2)      # 查找字符串，默认从第0个开始
        self.assertEqual('_abcabc_'.find("bc",3), 5)    # 指定从第3个开始

        self.assertEqual(" abc ".lstrip(), "abc ")      # 删除左边空格
        self.assertEqual(" abc ".rstrip(), " abc")      # 删除右边空格
        self.assertEqual(" abc ".strip(),  "abc")       # 删除前后边空格
        self.assertEqual("abbbc".strip('ac'), "bbb")    # 删除指定的前后缀字符
        

if __name__ == "__main__":
    unittest.main()