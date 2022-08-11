def printText():
    print('Hello world')

printText()


r = 10
s = 3.1415*(r**2)
print(s)

def sqRing(p):
    s = 3.1415 * (p ** 2)
    print(s)

sqRing(10)


def getSquare(w, h):
    return 2*(w+h), w*h

print(getSquare(5, 6))


def printText1(msg, end = '!', sep = ': '):
    print('Message' + sep + msg + end)

printText1('Text')
printText1('Text', '?')
printText1('Text', '?', ' ')
printText1('Text', sep = ' ')


def funct(a, b, c):
    '''
    :param a:
    :param b:
    :param c:
    :return:
    '''
    return a+b+c

help(funct)

