import time
import datetime


def tagMaker(func):
    def wrapper(*args, **kwargs):
        print('<div>')
        func(*args, **kwargs)
        print('</div>')

    return wrapper

@tagMaker
def printText(text):
    print(text)

tag1 = tagMaker(printText)

tag1('Hello')


def recTime(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        done = datetime.datetime.now() - start
        print(f'Функция завершена за {done} секунд')

    return wrapper

@recTime
def sfunc():
    time.sleep(3)
    print('Завершено')


sfunc()













