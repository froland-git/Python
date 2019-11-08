##############################
#user_names.txt#
##############################
#Переменная для файла
inputfile1 = "./user_names.txt"

#Вывод содержимого файла
myfile1 = open(inputfile1, mode='r', encoding='ascii')
#print(myfile.read()) #Прочитать файл можно только один раз. Если тут раскомментировать, то print в строке 11 выведет пустоту
print("-------------")

#Построчное чтение файла
#for line1 in myfile1:
#    print("Hello, " + line1.strip()) #strip убирает все символы в конце (\n)
#print("-------------")

#Построчное чтение файла и нумерация строк
for num1, line1 in enumerate(myfile1, 1): # enumerate -> num | myfile -> line | начинать с 1
    if "Lovette Rised" in line1:
        print("Line N: " + str(num1) + " : " + line1.strip())
print("-------------")

##############################
#list_of_password.txt#
##############################
inputfile2 = "./list_of_passwords.txt"
outputfile2 = "./my_passwords.tst"

password_to_look_for = "fdvdfvdv"

myfile21 = open(inputfile2, mode='r', encoding='ascii')
myfile22 = open(outputfile2, mode='w', encoding='ascii') # w - для записи | Создастся пустой файл

#write - всегда перезаписывает содержимое файла
#Чтобы добавлять в файл нужно a - append

#Построчное чтение файла и нумерация строк
for num2, line2 in enumerate(myfile21, 1): # enumerate -> num | myfile -> line | начинать с 1
    if password_to_look_for in line2:
        print("Line N: " + str(num2) + " : " + line2.strip())
        myfile22.write("Found password: " + line2)
print("-------------")

#Лучше закрывать файлы
myfile1.close()
myfile21.close()
myfile22.close()


