x = 25

#If
if x == 25:
    print("Good story 1")
else:
    print("Bad story 1")
print("##### END EX 1#####")

age = 31

if (age <= 4):
    print("You are baby")
elif (age > 4) and (age < 12):
    print("You are kid")
elif (age >= 12) and (age < 19):
    print("You are teenager")
else:
    print("You are old")
print("##### END EX 2#####")

all_cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']
german_cars = ['bmw', 'vw', 'skoda']

if "lada" in all_cars:
    print("Yes, Lada is in the list")
else:
    print("Lada in not in the list")
print("##### END EX 3#####")

for xxxx in all_cars:
    if xxxx in german_cars:
        print(xxxx + "is in German cars")
    else:
        print(xxxx + "is not German car")
print("##### END EX 4#####")