#! python3
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pw.py
@Time    :   2020/05/28 10:19:51
@Author  :   Darren 
@Version :   1.0
@Contact :   734876157@qq.com
@License :   (C)Copyright 2020, Darren
@Desc    :   # pw.py - An insecure password locker program.
'''

# here put the import lib
import sys
import pyperclip

# 命令行参数将存储在变量 sys.argv 中。sys.argv 列表中的第一项总是一个字符串，它包含程序的文件名
# （'pw.py'）。第二项应该是第一个命令行参数。
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
            'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt', 
            'wechat': '12345'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password') 
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
    

