#Есть файл из которого нужно достать только почтовые адреса
import re

input_filename = "./dumpfile.txt" #Инициализируем файл
result_filename = "results.txt"

inputfile = open(input_filename, mode='r',encoding="ascii") #Открываем файл
resultfile = open(result_filename, mode='w',encoding="ascii")

mytext = inputfile.read()#Читаем файл

lookfor = r"[\w.-]+@(?!intel\.com)[A-Za-z-]+\.[\w.]+" #RegExp для нахождения почтового адреса | ?! - исключение (?!intel\.com)


results = re.findall(lookfor,mytext)

for item in results:
    print(item)
    resultfile.write(item + "\n") #Построчное сохранение в файл

#resultfile.write()

print("Total: " + str(len(results)))

