#! python3
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ex7_strip.py
@Time    :   2020/05/29 10:12:11
@Author  :   Darren 
@Version :   1.0
@Contact :   734876157@qq.com
@License :   (C)Copyright 2020, Darren
@Desc    :   正则实现strip()功能
'''

# here put the import lib
import re

# param: str, delStr
# regex = re.compile(r'^( )+|( )+$')
# newStr = regex.sub('', '  he  llo  ')
# print(newStr)
def strip(s, ds=''):
    
    if type(s) != str or type(ds) != str:
        return 'Error: s or ds must be a str type param'
    else:
        if ds == '':
            regex = re.compile(r'^( )+|( )+$')
            return regex.sub('', s)
        else:
            regex = re.compile(r'[%s]'%ds)
            return regex.sub('', s)

a = strip('hello', 1)
print(a)


