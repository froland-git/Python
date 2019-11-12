#Библиотека
from urllib import request, parse #Импортируем только два модуля из библиотеки
import sys

myUrl = "https://www.google.com/search?" #Строка для поиска в Google
value = {'q':'Python'}

myheader = {}
myheader ['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'

try:
    #Преобразовываем к виду: q=Python
    mydata = parse.urlencode(value)
    print(mydata)
    #Преобразовываем к виду: https://www.google.com/search?q=Python
    myUrl = myUrl + mydata
    #Добавляем Header к запросу, чтобы показать, что это делает человек
    req = request.Request(myUrl, headers = myheader)
    #Обрабатываем ответ
    otvet = request.urlopen(req)
    otvet = otvet.readlines()
    #Вывод ответа
    for line in otvet:
        print (line)
    print("-------------------------")
except Exception:
    print("Error occuired during WEB-request!!!")
    print("Error Code: " + str(sys.exc_info()[1]))


