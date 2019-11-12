#Библиотека
from urllib import request #Импортируем только один модуль из библиотеки
import sys

myUrl = "<>" #Откуда скачать
myFile = "G:\\MyPython\\MyDownloads\\mykartinka.jpg" #Куда скачивать

try:
    print("Start Downloading file from: " + myUrl)
    request.urlretrieve(myUrl, myFile)
except Exception:
    print("AHTUNG!!!")
    print("Error Code: " + str(sys.exc_info()[1]))
    exit

print("File Downloaded and saved at: " + myFile)