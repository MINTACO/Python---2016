# 模式匹配与正则表达式
import re

# 向 re.compile()传入一个字符串值，表示正则表达式，它将返回一个 Regex 模式对象（或者就简称为 Regex 对象）。

# 手机号码的Regex对象
# phoneNumRegex = re.compile(r'(\d{3})-(\d{4})-(\d{4})')

# 匹配Regex对象
# search()
# Regex 对象的 search()方法查找传入的字符串，寻找该正则表达式的所有匹配。
# 如果字符串中没有找到该正则表达式模式，search()方法将返回 None。如果找到了该模式，search()方法将返回一个 Match 对象。
# Match 对象有一个 group()方法，它返回被查找字符串中实际匹配的文本

# 添加括号将在正则表达式中创建“分组”：(\d\d\d)-(\d\d\d-\d\d\d\d)。
# 第一对括号是第 1 组。第二对括号是第 2 组。
# 向 group()匹配对象方法传入整数 1 或 2，就可以取得匹配文本的不同部分。向 group()方法传入 0 或不传入参数，将返回整个匹配的文本。
# mo = phoneNumRegex.search('181-6869-8679')
# print('Phone number found: ' + mo.group())
# print(mo.group(1))
# 一次性获取全部分组，用mo.groups(),返回多个值的元组，所以可以使用多重赋值的技巧，每个值赋给一个独立的变量。
# areaCode, mainNumber, lastCode = mo.groups()
# print(areaCode, mainNumber, lastCode)
#匹配括号要进行转义
# phoneNumRegex1 = re.compile(r'(\(\d{3}\))-(\d{4})-(\d{4})')
# mo1 = phoneNumRegex1.search('(181)-6869-8679')
# print(mo1.group())


# 用管道符 | 匹配多个分组
# 希望匹配许多表达式中的一个时，就可以使用它
# 第一次出现的匹配文本，将作为 Match 对象返回
# 利用 findall()方法，可以找到“所有”匹配的地方
# heroRegex = re.compile (r'Batman|Ironman')
# mo = heroRegex.search('Batman and Ironman.')
# print(mo.group())

# 也可以使用管道来匹配多个模式中的一个，作为正则表达式的一部分。
# 因为所有这些字符串都以 Bat 开始，所以如果能够只指定一次前缀，就很方便。
# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
# print(mo.group())
# print(mo.group(1))


# 用问号实现可选匹配
# 字符?表明它前面的分组在这个模式中是可选的。
# 匹配这个问号之前的分组零次或一次
# batRegex = re.compile(r'Bat(wo)?man')
# mo = batRegex.search('The Adventures of Batman')
# print(mo.group())


# 用星号匹配零次或多次
# * 号之前的分组可以出现任意次（包括不存在）


# 用加号匹配一次或多次
# 加号前面的分组必须“至少出现一次”


# 用花括号匹配特定次数
# 如果想要一个分组重复特定次数，就在正则表达式中该分组的后面，跟上花括号包围的数字。
# 例如，正则表达式(Ha){3}将匹配字符串'HaHaHa'，但不会匹配'HaHa'，因为后者只重复了(Ha)分组两次。
# 除了一个数字，还可以指定一个范围，即在花括号中写下一个最小值、一个逗号和一个最大值。
# 例如，正则表达式(Ha){3,5}将匹配'HaHaHa'、'HaHaHaHa'和'HaHaHaHaHa'。


# 贪心和非贪心匹配
# Python 的正则表达式默认是“贪心”的，这表示在有二义的情况下，它们会尽可能匹配最长的字符串。
# 花括号的“非贪心”版本匹配尽可能最短的字符串，即在结束的花括号后跟着一个问号。
# greedyHaRegex = re.compile(r'(Ha){3,5}')
# nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
# mo1 = greedyHaRegex.search('HaHaHaHaHa')
# mo2 = nongreedyHaRegex.search('HaHaHaHaHa')

# print(mo1.group())
# print(mo2.group())
# 问号在正则表达式中可能有两种含义：声明非贪心匹配或表示可选的分组。这两种含义是完全无关的。


# findall()方法
# search()将返回一个Match对象，包含被查找字符串中的“第一次”匹配的文本，
# 而 findall()方法将返回一组字符串，包含被查找字符串中的所有匹配。
# findall()不是返回一个 Match 对象，而是返回一个字符串列表

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
# print(mo.group())

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
l = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(l)