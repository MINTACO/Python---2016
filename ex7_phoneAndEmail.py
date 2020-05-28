#! python3
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ex7_phoneAndEmail.py
@Time    :   2020/05/28 20:47:44
@Author  :   Darren 
@Version :   1.0
@Contact :   734876157@qq.com
@License :   (C)Copyright 2020, Darren
@Desc    :   Finds phone numbers and email addresses on the clipboard.
'''

# here put the import lib
import pyperclip, re

phoneRegex = re.compile(r'''
    ()
''')
