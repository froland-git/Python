#Это один объект
#       (-----Item-----)
#       (key)    (value)
#Словарь - это неупорядоченный набор элементов
enemy = {
            'loc_x': 70,
            'loc_y': 50,
            'color': 'green',
            'health': 100,
            'name': 'MAIN_ENEMY',
            'awards': ['Za honor', 'Za loyalty'],
            'image': ['image1.jpg', 'image2.jpg', 'image3.jpg']
}

#Копируем наш объект
all_enemies = []
my_all_enemies = []

all_enemies.append(enemy)
all_enemies.append(enemy)
all_enemies.append(enemy)
print(all_enemies)
print("##### END EX 1#####")

for x in range(0, 5):
   all_enemies.append(enemy)
   #Если хотим не клонировать элемент, а добавлять его копию, то all_enemies.append(enemy.copy())
print(all_enemies)
print("##### END EX 2#####")

for y in all_enemies:
    print(y)
print("##### END EX 3#####")

#Изменение элемента в массиве, члены которого - словари
all_enemies[2]['health'] = 30 #Менять только у второго, если в строке 26 используется all_enemies.append(enemy.copy())
print(all_enemies)
print("##### END EX 4#####")

#Когда элементы массива не клонируются
for y in all_enemies:
    print(y)
print("##### END EX 5#####")

enemy['loc_x'] = enemy['loc_x'] + 40


########################################
for z in range(0, 3):
   my_all_enemies.append(enemy.copy())

for t in my_all_enemies:
    print(t)
print("##### END EX 6#####")

my_all_enemies[0]['name'] = 'MAIN_ENEMY_1'
#my_all_enemies[0]['image'] = my_all_enemies[0]['image'].append('NEW_IMAGE.JPG') Так нельзя
my_all_enemies[0]['image'] = my_all_enemies[0]['image'] + ['NEW_IMAGE.JPG']

for k in my_all_enemies:
    print(k)
print("##### END EX 7#####")

print(my_all_enemies[0])
print(my_all_enemies[0]['image'])
print(type(my_all_enemies[0]['image']))
print("##### END EX 8#####")
