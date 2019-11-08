mystring = "Bla bla bla"
name = "ivan ivanov"
print(name.title()) #title() пишет каждое слово с большой буквы
print(name.upper()) #upper() делает все буквы заглавными
print(name.lower()) #lower() делает все буквы маленькими

print("Privet, stroka nomer 1 \nPrivet, stroka nomer 2\n\n")
print("Messages:\n\tMessage1\n\tMessage2\n\tMessage3\nEND")
print("Upper name:" + name.upper())

a = "    ...Ivan Ivanov...      "
b = "...Ivan Ivanov..."
print(a)
#Убираем пробелы
print(a.rstrip()) #справа
print(a.lstrip()) #слева
print(a.strip()) #все

 #Убираем точки
a = a.strip()
a = a.strip(".") 
print(a)