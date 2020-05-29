import os

# 1B（字节）=8bit（位）
# 1KB=1024B
# 1MB=1024KB
# 1GB=1024MB

# 读写文件

# 当程序运行时，变量是保存数据的好方法，但如果希望程序结束后数据仍然保持，就需要将数据保存到文件中。


# os.path.join()
# 将单个文件和路径上的文件夹名称的字符串传递给它，os.path.join()就会返回一个文件路径的字符串，包含正确的路径分隔符。
# windows系统为\，linux和mac os为/
# print(os.path.join('c', 'learn', 'style')) # 'c\\learn\\style'
# 双反斜杠\\，因为\需要转义
# myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
# for filename in myFiles:
#     print(os.path.join('C:\\Users\\asweigart', filename))


# 当前工作目录
# os.getcwd()
# print(os.getcwd())
# 并可以利用 os.chdir()改变它
# os.chdir('C:\\Windows\\System32')


# 绝对路径与相对路径
# • “绝对路径”，总是从根文件夹开始。
# • “相对路径”，它相对于程序的当前工作目录。
    # .\   代表这个目录（当前目录）
    # ..\  代表父级目录


# 创建新文件夹
# os.makedirs()
# os.makedirs('D:\\learn\\python书\\hello')
# os.makedirs()将创建所有必要的中间文件夹，目的是确保完整路径名存在。


# os.path 模块
# os.path 模块包含了许多与文件名和文件路径相关的有用函数。

    # 处理绝对路径和相对路径
    # os.path.abspath(path)将返回参数的绝对路径的字符串。这是将相对路径转换为绝对路径的简便方法。
    # os.path.isabs(path)，如果参数是一个绝对路径，就返回 True，如果参数是一个相对路径，就返回 False。
    # os.path.relpath(path, start)将返回从 start 路径到 path 的相对路径的字符串。如果没有提供 start，就使用当前工作目录作为开始路径。
# print(os.path.abspath('.'))
# print(os.path.isabs('.'))
# print(os.path.isabs(os.path.abspath('.')))
# >>> os.path.relpath('C:\\Windows', 'C:\\')
# 'Windows'
# >>> os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
# '..\\..\\Windows'

    # os.path.dirname(path)将返回一个字符串，它包含 path 参数中最后一个斜杠之前的所有内容。
    # os.path.basename(path)将返回一个字符串，它包含 path 参数中最后一个斜杠之后的所有内容。
    # os.path.split()，获得上面两个字符串的元组
    # os.path.sep 为当前系统的分隔符

    # split(os.path.sep)将路径拆分为字符串列表
# print('C:\\Windows\\System32'.split(os.path.sep))

    # 查看文件大小和文件夹内容
    # os.path.getsize(path)将返回 path 参数中文件的字节数。
    # os.listdir(path)将返回文件名字符串的列表，包含 path 参数中的每个文件。
        # （请注意，这个函数在 os 模块中，而不是 os.path）。
# print(os.path.getsize('.\\ex_8.py'))
# print(os.listdir('.\\'))

# totalSize = 0
# for fileNmae in os.listdir('.\\'):
#     totalSize += os.path.getsize(os.path.join('.', fileNmae))
# print(str(round(totalSize / 1024**2, 2)) + ' MB')

    # 检查路径有效性
    # os.path 模块提供了一些函数，用于检测给定的路径是否存在，以及它是文件还是文件夹。
    # 如果 path 参数所指的文件或文件夹存在，调用 os.path.exists(path)将返回 True，否则返回 False。 
    # 如果 path 参数存在，并且是一个文件，调用 os.path.isfile(path)将返回 True，否则返回 False。
    # 如果 path 参数存在，并且是一个文件夹，调用 os.path.isdir(path)将返回 True，否则返回 False。


    # 文件读写过程
    # 纯文本文件”只包含基本文本字符，不包含字体、大小和颜色信息
    # “二进制文件”是所有其他文件类型，诸如字处理文档、PDF、图像、电子表格和可执行程序。

# 在 Python 中，读写文件有 3 个步骤： 
#     1．调用 open( 绝对路径/相对路径 )函数，返回一个 File 对象。
#     2．调用 File 对象的 read()或 write()方法。
#     3．调用 File 对象的 close()方法，关闭该文件。

# helloFile = open('.\\hello.txt', 'r') #纯文本，读模式
# helloContent = helloFile.read() #读取为字符串
# helloContentLine = helloFile.readlines() #读取为每一行的字符串列表
# print(helloContent)
# print(helloContentLine)

# helloFile = open('.\\hello.txt', 'w') #纯文本，写模式
# helloFile = open('.\\hello.txt', 'a') #纯文本，添加模式
# 如果传递给 open()的文件名不存在，写模式和添加模式都会创建一个新的空文件。在读取或写入文件后，调用 close()方法，然后才能再次打开该文件。
# helloFile = open('.\\hello.txt', 'w')
# helloFile.write('Hello World!')
# helloFile.close()


#利用 shelve 模块，你可以将 Python 程序中的变量保存到二进制的 shelf 文件中。这样，程序就可以从硬盘中恢复变量的数据。
import shelve

# shelfFile = shelve.open('mydata') #传入文件名，不必指定模式
# cats = ['Zophie', 'Pooka', 'Simon']
# shelfFile['cats'] = cats
# shelfFile.close()

# shelfFile = shelve.open('mydata')
# print(type(shelfFile))
# print(type(shelfFile['cats']))
# print(list(shelfFile.keys()))
# print(list(shelfFile.values()))





