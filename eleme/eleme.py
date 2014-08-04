# coding=utf-8
__author__ = 'sennes'

import random
propt = ">>>>"
flag = True
welcome = """
欢迎来到饿了么roll点取外卖系统
通过roll点来决定谁去拿外卖或者洗锅是最公平的啦
本系统可以生成0-100的随机数，roll到数字最小的人就去拿外卖吧!
"""
small = 999
print welcome
while flag :
    roll = random.randint(0,100)
    check = raw_input(propt)
    if check == "q" :
        flag == False
        break
    if roll < small :
        small = roll
        print "%d 为人民服务!!!" %roll
    else :
        print roll
        pass

