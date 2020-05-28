def collatz(number):
    if number%2 == 0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1



def func(num):
    result = collatz(num)
    if result == 1:
        return 
    func(result)

try:
    intNum = int(input('Please enter an integer:'))
    func(intNum)
except ValueError:
    print('You should enter an integer')
    








