# 字典dict和结构化数据

# 无序，不可切片
import pprint

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

# print(myCat.keys())
# print(myCat.values())
# print(myCat.items())
# print(list(myCat.keys()))
# print(list(myCat.values()))
# print(list(myCat.items()))

# for x, y in myCat.items():
#     print(x + ':' + y)

# print('size' in myCat)

# get()方法，它有两个参数：要取得其值的键，以及如果该键不存在时，返回的备用值。
# print(myCat.get('name', 'MIMI'))

# setdefault()方法,为字典中某个键设置一个默认值，当该键没有任何值时使用它。
# 第一个参数，是要检查的键。第二个参数，是如果该键不存在时要设置的值。
# myCat.setdefault('name', 'MIMI')
# myCat.setdefault('name', 'TIMI') #重复的键只会生效一次，因为已经有值
# print(myCat)

# 小程序，计算一个字符串中每个字符出现的次数。
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1

# a = pprint.pformat(count)  
# print(a)
# pprint.pprint(count)


# 井字棋(字典数据结构简单应用)
# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
# def printBoard(board):
#     print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
#     print('-+-+-')
#     print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
#     print('-+-+-')
#     print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
# turn = 'X'
# for i in range(9):
#     printBoard(theBoard)
#     print('Turn for ' + turn + '. Move on which space?')
#     move = input()
#     theBoard[move] = turn
#     if turn == 'X':
#         turn = 'O'
#     else:
#         turn = 'X'

# printBoard(theBoard)


# 多重字典（嵌套）
# allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
#             'Bob': {'ham sandwiches': 3, 'apples': 2},
#             'Carol': {'cups': 3, 'apple pies': 1}}


# 计算所有客人带来的每种水果个数
# def fruitNum(guests, kind):
#     num = 0
#     for k, v in guests.items():
#         num += v.get(kind, 0)
#     return num

# print(fruitNum(allGuests, 'apples'))





# 实践项目
# 1.物品清单
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(l):
    print('Inventory:')
    num = 0
    for k, v in l.items():
        num += v
        print(v, k)
    print('Total:' + str(num))

# displayInventory(inventory)

# 2.加入战利品（list）
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for i in addedItems:
        inventory.setdefault(i, 0)
        inventory[i]+=1

addToInventory(inventory, dragonLoot)
displayInventory(inventory)