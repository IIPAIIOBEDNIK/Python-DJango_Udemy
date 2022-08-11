a, *b, c = 10, 20, 30, 'Text', 3.14, True

print(a)
print(b)
print(c)


s = [4, 10]
print(list(range(*s)))

def func(a,b,c,d):
    print(a,b,c,d)

a = ('Hello', True, 3.14, [3,4,5])

func(*a)


def func1(*args):                               #Для неименованых аргументов
    print(sum(args)*0.06)

func1(10, 2, 3.14, 8, 9)


def func2(*args, **kwargs):
    print(args)
    print(kwargs)

func2(1, 2, 5.17, a=1, b=2, c=3)











