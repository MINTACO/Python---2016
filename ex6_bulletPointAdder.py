#! python3
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   bulletPointAdder.py
@Time    :   2020/05/28 10:34:04
@Author  :   Darren 
@Version :   1.0
@Contact :   734876157@qq.com
@License :   (C)Copyright 2020, Darren
@Desc    :   从剪贴板中取得文本，在每一行开始处加上星号和空格，然后将这段新的文本贴回到剪贴板。
'''

# here put the import lib
import pyperclip

text = pyperclip.paste()
l = text.split('\n')
for i in range(len(l)):
    l[i] = '* ' + l[i] 
   
text = '\n'.join(l)
# print(text)

pyperclip.copy(text)