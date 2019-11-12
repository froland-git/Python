import pygame

#Параметры экрана
MAX_X = 800
MAX_Y = 600
game_over = False
bg_color = (0, 0, 0) # Базовый цвет - черный

x = 150 #Первоначальное расположение картинки по x
y = 150 #Первоначальное расположение картинки по y

#pygame.init()
#screen = pygame.display.set_mode((MAX_X, MAX_Y), pygame.FULLSCREEN) # На весь экран
screen = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption("My first PyGame! :)")

#print(pygame.image.get_extended()) #Возвращает true или false, то есть проверяем, можем ли мы загрузить картинку или нет

myimage = pygame.image.load("Picture26.PNG").convert() #Загружаем картинку
myimage = pygame.transform.scale(myimage, (350,350)) #Уменьшение размеров исходной картинки

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
                x -= 20
            if event.key == pygame.K_RIGHT:
                x += 20
            if event.key == pygame.K_UP:
                y -=20
            if event.key == pygame.K_DOWN:
                y +=20  
        #Нажатие мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos #Картинка будет там, где будет курсор

    screen.fill(bg_color) #Закрашиваем старое изображение картинки перед ее отрисовкой
    screen.blit(myimage, (x, y)) #x = 100, y = 100 | Вывод на экран картинки
    pygame.display.flip()




