# 字符串操作

# 字符串可以以双引号开始和结束，里面可以包括单引号
# spam = "That is Alice's cat."

# 也可以用转义字符\
# \'  \"  \t  \n  \\
#  spam = 'Say hi to Bob\'s mother.'

# 原始字符串 r''
# 忽略字符串中所有的转义字符
# 多用于正则表达式
# print(r'That is Carol\'s cat.')

# 多行字符串
# “三重引号”之间的所有引号、制表符或换行，都被认为是字符串的一部分。Python 的代码块缩进规则不适用于多行字符串。
# print('''Dear Alice,


# Eve's cat has been arrested for catnapping, cat burglary, and extortion. 


# Sincerely,
# Bob''')


#多行注释 ***  ***


# 字符串像列表一样，使用下标和切片
# 字符串切片并没有修改原来的字符串。可以从一个变量中获取切片，记录在另一个变量中。


# 像列表一样，in 和 not in 操作符也可以用于字符串。用 in 或 not in 连接两个字符串得到的表达式，将求值为布尔值 True 或 False。


# 有用的字符串方法
# upper()  lower()  isupper()  islower()
# upper()和 lower()字符串方法返回一个新字符串，其中原字符串的所有字母都被相应地转换为大写或小写。字符串中非字母字符保持不变。
# spam = 'Hello world!'
# print(spam.upper(), spam.lower())
# 可实现无大小写的比较
# 如果字符串至少有一个字母，并且所有字母都是大写或小写，isupper()和islower()方法就会相应地返回布尔值 True。
# print(spam.islower())
# 可链式调用（方法本身返回新的字符串）
# spam.lower().upper()


# isalpha()返回 True，如果字符串只包含字母，并且非空； 
# isalnum()返回 True，如果字符串只包含字母和数字，并且非空；
# isdecimal()返回 True，如果字符串只包含数字字符，并且非空；
# isspace()返回 True，如果字符串只包含空格、制表符和换行，并且非空；
# istitle()返回 True，如果字符串仅包含以大写字母开头、后面都是小写字母的单词

# while True:
#     print('Enter your age:')
#     age = input() 
#     if age.isdecimal():
#         break 
#     print('Please enter a number for your age.')
# while True:
#     print('Select a new password (letters and numbers only):')
#     password = input()
#     if password.isalnum():
#         break 
#     print('Passwords can only have letters and numbers.')


#startswith()和 endswith()方法返回 True，如果它们所调用的字符串以该方法传入的字符串开始或结束。否则，方法返回 False。


# ''.join()  字符串列表 => 字符串
# split()   字符串 => 字符串列表  默认情况下，字符串'My name is Simon'按照各种空白字符分割，诸如空格、制表符或换行符。
# print( ', '.join(['cats', 'rats', 'bats']))
# print('cats, rats, bats'.split(','))


# rjust()、ljust()和 center()方法对齐文本
# print('hello'.rjust(10, '*'))
# print('hello'.ljust(10, '*'))
# print('hello'.center(11, '*'))


# strip()、rstrip()和 lstrip()删除 开头末尾/开头/末尾 空白字符，返回新的字符串
# 有一个可选的字符串参数，指定两边的哪些字符应该删除。
# 向 strip()方法传入参数'ampS'，告诉它在变量中存储的字符串两端，删除出现的a、m、p 和大写的 S。传入 strip()方法的字符串中，字符的顺序并不重要：strip('ampS')做的事情和 strip('mapS')或 strip('Spam')一样。
# spam = 'SpamSpamBaconSpamEggsSpamSpam'
# print(spam.strip('ampS'))


# pyperclip 模块有 copy()和 paste()函数，可以向计算机的剪贴板发送文本，或从它接收文本。
# import pyperclip

# pyperclip.copy('hello')
# pyperclip.paste()



#实践项目，表格打印，右对齐
import copy

tableData = [['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'], 
            ['dogs', 'cats', 'moose', 'goose']]

def printTable(l):
    length = len(l[0])
    lengthList = []
    tempL = copy.deepcopy(l)
    
    for i in l:
        i.sort(key = lambda x:len(x))
        lengthList.append(len(i[-1]))
    
    # print(tempL)
    for i in range(length):
        for j in tempL:
            print(j[i].rjust(lengthList[tempL.index(j)]), end=' ')
        print('\n')
    
printTable(tableData)

