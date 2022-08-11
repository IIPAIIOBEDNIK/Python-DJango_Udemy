# List - Список

list_1 = ['anna', 'alex', 'max']
list_2 = ['john', 'nicolas', 'vlad']
print(list_1 + list_2)

list_1[0] = 'artur'                 #Замена 0-го элемента на artur
print(list_1)

list_1.append('anna')               #Добавление anna в конец списка
print(list_1)

list_1.insert(1, 'john')            #Добавление john на позицию 1-го элемента
print(list_1)

print(list_1.index('max'))          #Поиск позиции элемента в списке
list_1.index('max', 0, 10)          #Поиск элемента max в указанном диапазоне

pop_del = list_1.pop()              #Удаляет последний элемент списка
print(pop_del)
print(list_1)

list_1.pop(0)                       #Удаление 0-го элемента
print(list_1)

list_1.clear()                      #Очистка списка
print(list_1)


list_3 = ['33', '22', '11', '44']
print(list_3)

list_3.sort()                       #Сортировка списка по возрастанию
print(list_3)

list_3.sort(reverse=True)           #Сортировка по убыванию
print(list_3)


list_4 = ['abcde', 'bcb', 'da', 'cde', 'ser', 'q']
print(list_4)

list_4.sort()                       #Сортировка по возрастанию
print(list_4)

list_4.sort(key=len)                #Сортировка по длине символов
print(list_4)

list_4.reverse()                    #Реверсирует список
print(list_4)



