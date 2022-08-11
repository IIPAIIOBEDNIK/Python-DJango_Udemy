#Set - Множество - последовательность уникальных объектов

first_set = {'Alex', 'John', 'Georg', 'Alex'}
print(type(first_set))
print(first_set)
print(len(first_set))                                   #Просмотр количества элементов в множестве

first_set.add('Maxim')                                  #Добавление элемента во множество
print(first_set)

first_set.remove('Alex')                                #Удаление элемента из множества
print(first_set)

first_set.clear()                                       #Полная очистка множества
print(first_set)



first_set = {'Alex', 'John', 'Georg', 'Alex'}
second_set = {'Anton', 'Tom', 'Anna', 'Alex'}
third_set = first_set.union(second_set)                 #Объединение двух множеств
print(third_set)

fourth_set = first_set.intersection(second_set)         #Выводит объекты присутствующие одновременно в сравниваемых множествах
print(fourth_set)

fifth_set = first_set.difference(second_set)            #Выводит объекты первого множества, которых нет во втором множестве
print(fifth_set)
print(fifth_set - second_set)                           #Аналог вывода элементов отсутствующих во втором множестве

set_1 = {1, 2, 3}
set_2 = {1, 2, 3, 4, 5}
print(set_1.issubset(set_2))                            #Проверка является первое множество подмножеством второго множества
print(set_2.issuperset(set_1))                          #Проверка является второе множество надмножеством первого множества





