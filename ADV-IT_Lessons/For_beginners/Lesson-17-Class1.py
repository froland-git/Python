import hero

#####MAIN#####
#Теперь собственно создание самого объекта:
myhero1 = hero.Hero("Vurdalak", 5, "Orc")
myhero2 = hero.Hero("Alexander", 4 , "Human")

#Передача методов
#Перед каждой строкой писать hero.myhero1.show_hero() не обязательно, так как уже написано тут, что брать из Hero myhero1 = hero.Hero("Vurdalak", 5, "Orc")
myhero1.show_hero()
myhero2.move()
myhero1.level_up()
myhero1.show_hero()
#myhero1.healthinit = 70 #Так не делать, лучше создать метод set_health
myhero1.set_health(60)
myhero1.show_hero()