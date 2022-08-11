#Dict - Словарь

students = {
    'alex' : 258,
    'max' : 227,
    'anna' : 278
}
print(students)

print(students['anna'])                         #Чтение значения по ключу
print(students.get('alex'))

students['andrey'] = 268                        #Добавление нового элемента в конец словаря
print(students)

students['andrey'] = 177                        #Обновление значения в словаре
print(students)

students.setdefault('oleg')                     #Добавление нового ключа без значения(c пустым значением)
print(students)

students.pop('oleg')                            #Удаление пары по ключу
print(students)

print(students.keys())                          #Получение всех ключей из словаря

print(type(students.keys()))                    #Определение типа ключей

key_list = list(students.keys())                #Вывод ключей словаря в список
print(key_list)
print(type(key_list))

print(students.values())                        #Вывод значений словаря
print(type(students.values()))

print('anna' in students)                       #Проверка ключа по словарю

print('peter' not in students)                  #Проверка отсутствия ключа в словаре









