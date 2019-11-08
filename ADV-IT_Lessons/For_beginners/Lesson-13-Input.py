name = input("Please, enter your name: ")
print("Privet," + name)

#input всегда считывает строки
num1 = input("Enter X: ")
num2 = input("Enter Y: ")

summa = int(num1) + int(num2)
print(summa)
print("##### END EX 1#####")

message = ""

while True:
    message = input("Enter Password: ")
    if message == "secret":
        break
    print(message + "Password not correct")

print("Password was: " + message)
print("##### END EX 2#####")

mylist = []
msg = ""

while msg != 'stop'.upper():
    msg = input("Enter new item, and STOP to finish: ")
    mylist.append(msg)

print (mylist)
print("##### END EX 3#####")


