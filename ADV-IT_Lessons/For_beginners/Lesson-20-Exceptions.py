import sys

filename = "./Lesson_List.txt"

#Перехват ошибок
try:
    print("Inside TRY")
    myfile = open(filename, mode='r', encoding='ascii')
except Exception: #Сюда, только еси будет ошибка
    print("Inside EXCEPT")
    print("Error Found")
    sys.exit() #Остановить выполнение программы
else:
    print("Inside ELSE")
    print(myfile.read())
finally:
    print("Inside FINALLY")

print("--------EOF--------")