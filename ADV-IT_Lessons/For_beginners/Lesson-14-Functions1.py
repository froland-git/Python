###################FUNCTIONS#####################
def napeshatat_privetstvie(name):
    """Print Privetstvie"""
    print("Congratulations, " + name + " wish you all best!")
    print("Best regards")


def summa(x, y):
    print(x + y)

def summa1(x, y): #входные параметры
    s = x + y
    return s #возвращает наружу

#Вычисление факториала
def factorial(x):
    """Calculate factorial for number x"""
    otvet = 1
    for i in range(1,x+1): #+1 так как множество незакрытое
        otvet = otvet * i
    return otvet

###################MAIN PROGRAM#####################
print("-------------------------------")
napeshatat_privetstvie("Denis")
napeshatat_privetstvie("Vasya")

print("-------------------------------")
summa(10,20)

print("-------------------------------")
summa(11,21)

print("-------------------------------")
print(factorial(3))

print("-------------------------------")
for i in range (1,10):
    print(str(i) + "!\t" + str(factorial(i)))


