#JSON - это библиотека

import json
filename = "./user_settings.txt"
myfile = open(filename,mode="w",encoding="ascii")

player1 = {
    'PlayerName': 'Donald Trump',
    'Score': 345,
    'Awards': ["OR", "NV", "NY"]
}

player2 = {
    'PlayerName': 'Clinton Hillary',
    'Score': 346,
    'Awards': ["WT", "TX", "MI"]
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

#---------SAVE by JSON---------
json.dump(myplayers,myfile) #myplayers - что сохраняем, myfile - куда сохраняем
myfile.close()

#---------LOAD from JSON---------
myfile = open(filename,mode="r",encoding="ascii")
json_data = json.load(myfile)

for user in json_data:
    print("Name player is: " + str(user['PlayerName']))
    print("Player score is: " + str(user['Score']))
    print("Player Award #1: " + str(user['Awards'][0]))
    print("Player Award #2: " + str(user['Awards'][1]))
    print("Player Award #3: " + str(user['Awards'][2]))
    print("-----------------------------------\n\n")