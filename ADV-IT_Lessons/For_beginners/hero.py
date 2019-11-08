##############################
#Lesson-17#
##############################

#Название файла с модулем должно быть как азвание класса, но с маленькой буквы

#Class объединяет словари (dictionary) и позволяет выполнить какие-либо функции над ними
#Функция в классе называется метод

class Hero():
    """Class to create hero for our game"""
    def __init__(self, name, level, race): # Этот метод всегда перый в классе | name, level, race - входные параметры от пользователя
        """Initiate our hero"""
        self.nameinit = name
        self.levelinit = level
        self.raceinit = race
        self.healthinit = 100 # Задаем вручную

    def show_hero(self):
        """Print all parameters of this Hero"""
        description = (self.nameinit + " Level is: " + str(self.levelinit) + " Race is: " + self.raceinit + " Health is: " + str(self.healthinit)).title()
        print (description)

    def level_up(self):
        """Upgrade Level of Hero"""
        self.levelinit = self.levelinit + 1

    def move(self):
        """Start moving hero"""
        print("Hero " + self.nameinit + " starts moving...")

    def set_health(self, new_health):
        self.healthinit = new_health 

#В итоге мы создали класс Hero
#При инициализации ему передаются параметры: name, level, race в качестве входных значений -> Создается объект
#Этому объекту передаются все аатрибуты  name, level, race и добавляется healthinit, которая только что объевляется
#Также у этого объекта есть три метода (функции в классе):
#   распечатать всю информацию show_hero
#   поднять уровень level_up
#   подвинуть move

##############################
#Lesson-18#
##############################
class SuperHero(Hero): #class Children_class(Parent_class)
    """Class to Create SUper Hero"""
    def __init__(self, name, level, race, magiclevel):
        """Initiate our SUper Hero"""
        super().__init__(name,level,race) #Наследование от класса Hero (родительского класса) | super делает наследование класса
        self.magiclevelsuperinit = magiclevel
        self.magic = 100
    
    #Новый метод, который не наследуется
    def makemagic(self):
        self.magic -= 10
    
    #Дополнение к функции, которая наследуется из класса Hero
    def show_hero(self): #Название оставляем тем же
        # + ("Magic is: " + self.magic)
        description = (self.nameinit + " Level is: " + str(self.levelinit) + " Race is: " + self.raceinit + " Health is: " + str(self.healthinit) + " Magic is: " + str(self.magic)).title()
        print (description)
