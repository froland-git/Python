#Библиотека
from urllib import request #Импортируем только один модуль из библиотеки

myUrl = "http://www.astahov.net"

#Лучше еще добавить модуль TRY
otvet = request.urlopen(myUrl)
mytext1 = otvet.readlines()
mytext2 = otvet.read()

print(otvet)
print("-------------------------")

print(mytext2)
print("-------------------------")

for line in mytext1:
    print(line)
print("-------------------------")

