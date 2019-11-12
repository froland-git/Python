#Дорабатываем движение картинки
#Нет события - УДЕРЖАНИЕ КНОПКИ
import pygame

#Параметры экрана
MAX_X = 800
MAX_Y = 600
IMG_SIZE = 350
game_over = False
bg_color = (0, 0, 0) # Базовый цвет - черный

x = 150 #Первоначальное расположение картинки по x
y = 150 #Первоначальное расположение картинки по y

#Флаги движения
move_right = False
move_left = False
move_up = False
move_down = False

#pygame.init()
#screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN) # На весь экран
screen = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption("My first PyGame! :)")

#print(pygame.image.get_extended()) #Возвращает true или false, то есть проверяем, можем ли мы загрузить картинку или нет

myimage = pygame.image.load("Picture26.PNG").convert() #Загружаем картинку
myimage = pygame.transform.scale(myimage, (IMG_SIZE,IMG_SIZE)) #Уменьшение размеров исходной картинки

#-------------MAIN GAME LOOP-------------
#Вывод картинки на экран:
while game_over == False:
    for event in pygame.event.get(): # Все события (например, движение мыши) в игре 
        #Нажатие клавиатуры
        if event.type == pygame.KEYDOWN: #Если нажать на любую кнопку клавиатуры (но не мыши) - выход 
            if event.key == pygame.K_ESCAPE: #Нажата ESC
                game_over = True
            #Перемещение картинки:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_UP:
                move_up = True
            if event.key == pygame.K_DOWN:
                move_down = True  
        
        #Отпускаем кнопку клавиатуры
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_UP:
                move_up = False
            if event.key == pygame.K_DOWN:
                move_down = False  
        
        #Нажатие мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos #Картинка будет там, где будет курсор
        
    #Изменение координат картинки:
    if move_left == True:
        x -= 1
        if x < 0:
            x = 0
    if move_right == True:
        x += 1
        if x > MAX_X - IMG_SIZE:
             x = MAX_X - IMG_SIZE
    if move_up == True:
        y -= 1
        if y < 0:
            y = 0
    if move_down == True:
        y += 1
        if y > MAX_Y - IMG_SIZE:
            y = MAX_Y - IMG_SIZE
    
    screen.fill(bg_color) #Закрашиваем старое изображение картинки перед ее отрисовкой
    screen.blit(myimage, (x, y)) #x = 100, y = 100 | Вывод на экран картинки
    pygame.display.flip()