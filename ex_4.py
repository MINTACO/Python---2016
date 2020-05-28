# 1.逗号代码
# param: list
def func(l):
    s = ''
    end = l.pop(len(l)-1)
    for i in l:
        s += (str(i) + ', ')
    print(s + 'and ' + str(end))

spam = ['apples', 'bananas', 'tofu', 'cats']

# num = [1,2,3,4]

# func(spam)

# 2.字符图网格
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
def printList(grid):
    a = []
    for i in range(6):
        a.append('\n')
    grid.append(a)
    for y in range(6):
        for x in grid:
            print(x[y], end='')

# def printList(grid):
printList(grid)
