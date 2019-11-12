#Библиотеки
import pygame
import random
import sys
import time #Чтобы сделать задержку

#Размер экрана
MAX_X = 1366
MAX_Y = 768

#Количество снежинок
MAX_SNOW = 150

#Размер снежинки
SNOW_SIZE = 64 #В пикселях

#Класс снежинки
class Snow():
    def __init__(self, x, y): #x и y - координаты снежинки
        """Инициализация снежинки"""
        self.xx = x
        self.yy = y
        self.speed = random.randint(5, 10) #От 5 до 10
        self.img_num = random.randint(1, 4)
        self.image_filename = "snow" + str(self.img_num) + ".PNG"
        self.image = pygame.image.load(self.image_filename).convert_alpha() #Загружаем картинку
        self.image = pygame.transform.scale(self.image, (SNOW_SIZE, SNOW_SIZE)) #Уменьшаем картинку по x и y на SNOW_SIZE
    
    def move_snow(self):
        """Перемещение снежинки"""
        self.yy = self.yy + self.speed #Движение снежинки вниз
        if self.yy > MAX_Y: #Если снежинка дошла до самого нижней границы экрана, то она должна появиться сверху
            self.yy = (0 - SNOW_SIZE)

        i = random.randint(1, 3)
        if i == 1: #Движение направо
            self.xx = self.xx + 10
            if self.xx > MAX_X:
                self.xx = (0 - SNOW_SIZE)
        elif i == 2: #Движение налево
            self.xx = self.xx - 10
            if self.xx < (0 - SNOW_SIZE):
                self.xx = MAX_X

    def draw_snow(self):
        screen.blit(self.image, (self.xx, self.yy))
        pygame.display.flip()
"""Конец класса Snow()"""

def initialize_snow(MAX_SNOW, snowfall):
    """Функция создает снежинки на экране"""
    #Теперь собственно создание массива объектов, используя класс
    for i in range(0, MAX_SNOW):
        xxx = random.randint(0, MAX_X)
        yyy = random.randint(0, MAX_Y)
        snowfall.append(Snow(xxx, yyy)) #Берем класс Snow и перекидываем туда координаты снежинки, так как def __init__(self, x, y) | затем добавляем в массив

def check_for_exit():
    """Функция, которая осуществляет выход"""
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()

#---------------------MAIN---------------------
#pygame.init
screen = pygame.display.set_mode((MAX_X, MAX_Y))
bg_color = (255, 255, 255) #0,0,0 - black | 255,255,255 - white
snowfall = [] #Для массива снежинок

initialize_snow(MAX_SNOW, snowfall)

while True:
    screen.fill(bg_color) #Закрашиваем старое изображение картинки перед ее отрисовкой
    check_for_exit()
    for i in snowfall:
        i.move_snow() #Передача методов
        i.draw_snow() #Передача методов
    time.sleep(0.10)
    pygame.display.flip()
