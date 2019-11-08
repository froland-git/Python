for x in range(0,10): # 10 не входит в диапазон
    print(x)
    print("***********")

for x in range(-4,10,2): # 10 не входит в диапазон c шагом 2
    print("Number x =" + str(x))
    print("***********")

for x in range(-4,10,2): # 10 не входит в диапазон c шагом 2
    print("Number x =" + str(x))
    print("***********")
    if x == 6:
        break #Выход
print("#####EOF#####")

x = 0
while True: #Бесконечный цикл
    print(x)
    x = x + 1
    if x == 5:
        break #Выход