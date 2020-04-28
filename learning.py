# -*- coding:utf=8 -*-

import argparse

"""
创建 ArgumentParser() 对象
调用 add_argument() 方法添加参数
使用 parse_args() 解析添加的参数
"""

#简单实例
# parser = argparse.ArgumentParser(description="position arg")
# parser.add_argument("interger", type=int, help="diplay interger")
# args = parser.parse_args()
#
# print(args.interger)


#定位参数
# parser = argparse.ArgumentParser()
# parser.add_argument("square", help="display a square of a given number", type=int)
# args = parser.parse_args()
# print(args.square**2)


#可选参数
# parser = argparse.ArgumentParser()
#
# parser.add_argument("--square", help="display a square of a given number", type=int)
# parser.add_argument("--cubic", help="display a cubic of a given number", type=int)
# args = parser.parse_args()
# if args.square:
#     print(args.square ** 2)
# if args.cubic:
#     print(args.cubic ** 3)


#混合使用
# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
#
# args = parser.parse_args()
# print(args.accumulate(args.integers))
