#       (-----Item-----)
#       (key)    (value)
#Словарь - это неупорядоченный набор элементов
enemy = {
            'loc_x': 70,
            'loc_y': 50,
            'color': 'green',
            'health': 100,
            'name': 'MAIN_ENEMY'
}

print(enemy)

print("Location X = " + str(enemy['loc_x']))
print("Location Y = " + str(enemy['loc_y']))
print("His name = " + str(enemy['name']))

#Добавление Items в Dictionary
enemy['rank'] = 'Admiral'
print(enemy)

#Удаление Items в Dictionary
del enemy['rank']
print(enemy)

#Изменение Items в Dictionary
enemy['loc_x'] = enemy['loc_x'] + 40
enemy['health'] = enemy['health'] + 30

if enemy['health'] > 110:
    enemy['color'] = 'gray'
print(enemy)

#Элементы словаря
print(enemy.keys())
print(enemy.values())