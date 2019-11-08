cities = ['NY', 'Moscow', 'new dehli', 'Simferopol', 'Toronto']
print(cities)
print (len(cities)) #Вывести длину массива /5
print(cities[0]) #Вывести один элемент массива /NY
print(cities[-1])#Вывести один элемент массива /Toronto с конца
print(cities[2].title()) #/New Dehli

#Замена элемента массива
cities[2] = 'Tula'
print(cities)

#Добавление элемента массива
cities.append('Kursk') #Добавление в конец
print(cities)
cities.insert(2, 'Feodosiya') #Добавление на 2 место
print(cities)

#Удаление элемента массива
del cities[-1] #Удаляем конечный элемент
print(cities)
cities.remove('Tula') #Единичное удаление по имени
print(cities)

#Вывод элемента, который удаляем
deleted_city = cities.pop()
print('Deleted city is:' + deleted_city)
print(cities)

#Сортировка
cities.sort() #В обратном порядке cities.sort(reverse=True)
print(cities)

#Поменять местами
cities.reverse()
print(cities)
