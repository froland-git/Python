#Работа с массивами, используя циклы
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

for x in cars:
    print(x.upper())
print("#####End Ex 1#####")

for x in range(1,6):
    print(x)

#Создание массива чисел с помощью цикла
mynumber_list = list(range(0,10))
print("New list: " + str(mynumber_list))

for x in mynumber_list: #Умножить каждый элемент массива на 2
    x = x * 2
    print(x)
print("#####End Ex 2#####")

#Сортировка в обратную сторону
mynumber_list.sort(reverse=True)
print(mynumber_list)
print("#####End Ex 3#####")

#Найти максимальную цифру в массиве
print("Max number is " + str(max(mynumber_list))) # min и sum аналогично
print("#####End Ex 4#####")

#Вырезать кусок массива
mycars = cars[1:3]
print(mycars)
print("#####End Ex 5#####")

#Неизменяемая копия массива
myextracars = cars[:]
print(myextracars)
print("#####End Ex 6#####")