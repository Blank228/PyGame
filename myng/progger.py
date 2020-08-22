import pygame
#инициализация библиотеки
pygame.init()
import time

#задаем разрешение экрана
win = pygame.display.set_mode((1214,686))

#Название игры в окне
pygame.display.set_caption('Progger')

#Параметры игрока х = 50
x = 50
y = 450
width = 200
height = 200
# speed = 15
speed = 50
scene = 2

clock = pygame.time.Clock()

citygif = [pygame.image.load('0.jpg'),
             pygame.image.load('1.jpg'),
             pygame.image.load('2.jpg'),
             pygame.image.load('3.jpg'),
             pygame.image.load('4.jpg'),
             pygame.image.load('5.jpg'),
             pygame.image.load('6.jpg')]

walkRight = [pygame.image.load('run_right1.png'),
             pygame.image.load('run_right2.png'),
             pygame.image.load('run_right3.png'),
             pygame.image.load('run_right4.png'),
             pygame.image.load('run_right5.png')]

walkLeft = [pygame.image.load('run_left1.png'),
             pygame.image.load('run_left2.png'),
             pygame.image.load('run_left3.png'),
             pygame.image.load('run_left4.png'),
             pygame.image.load('run_left5.png')]



playerStandR = pygame.image.load('stayright.png')
playerStandL = pygame.image.load('stayleft.png')
BG_arr = {
    1 : pygame.image.load('BG1.jpg'),
    2 : pygame.image.load('BG2.jpg'),
    3 : pygame.image.load('BG3.jpg')
}
BG = BG_arr[scene]
PDA = pygame.image.load('DenisMail.png')
WinWatch = pygame.image.load('WinWatch.png')
dur = pygame.image.load('Door.png')
ButF = pygame.image.load('fbut.png')
vibr = pygame.image.load('vibro.png')
book = pygame.image.load('book.png')
WinPass = pygame.image.load('WindowsPass.png')
Poster1 = pygame.image.load('poster1.jpg')
Poster2 = pygame.image.load('poster2.jpg')
Poster3 = pygame.image.load('poster3.jpg')
canon = pygame.image.load('canon.png')


#Текст про книгу
f1 = pygame.font.Font('BK0010.ttf', 36)
text1 = f1.render('Работа за ПК', 1, (255, 255, 255))

#Посмотреть в окно
f2 = pygame.font.Font('BK0010.ttf', 36)
text2 = f2.render('Посмотреть в окно', 1, (255, 255, 255))

#Выйти из комнаты
f3 = pygame.font.Font('BK0010.ttf', 36)
text3 = f3.render('Просмотреть ПДА', 1, (255, 255, 255))
#переменные миссий
PC = True
Okn = True
ExitFromRoom = True
first_dialog = True
bookquest = True
# PC = False
# Okn = False
# ExitFromRoom = False
# first_dialog = False
# bookquest = False


#Переменные ходьбы
left = False
right = False
animCount = 0
BigQ = 'Кажется, моему другу Денису нужна помощь!'
LitQ = 'Время освежить память и открыть книжку'
#ставим беграунд
def drawWindow():

    global animCount
    win.blit(BG, (0,0))
    if(scene == 1):
        win.blit(dur, (815, 69))


    if animCount +1>5:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount],(x,y))
        animCount +=1
    elif right:
        win.blit(walkRight[animCount],(x,y))
        animCount+=1
    else:
        win.blit(playerStandR,(x,y))


    if first_dialog == True:
        f4 = pygame.font.Font('BK0010.ttf', 45)
        fontdenhelp = pygame.font.Font('BK0010.ttf', 35)
        text4 = f4.render(BigQ, 1, (255, 255, 255))
        textdenhelp = fontdenhelp.render(LitQ,1, (255, 0, 191))
        win.blit(text4,(0,10))
        win.blit(textdenhelp,(0,40))



# флаг для одиночного срабатывания нажатия и отжатия
flag_key = True
def keyPress(flag):#Функция переключения состояния
    global flag_key
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_f and flag_key == False:
            flag_key = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_f and flag_key == True:
            flag_key = False
            flag = not flag
    return flag

def change_scene(x_coords, scene_id):
    global first_dialog
    global x, scene, BG
    if x_coords-50 < x and x < x_coords+50:
        if x_coords < 1214 / 2:
            desired_key = pygame.K_LEFT
        else:
            desired_key = pygame.K_RIGHT
        if event.type == pygame.KEYDOWN:
            if event.key == desired_key:
                if ExitFromRoom == True:
                    scene = scene_id
                    BG = BG_arr[scene_id]
                    if x_coords < 1214 / 2:
                        x = 1000
                    else:
                        x = -100

door_flag = False
#Подойти к двери
def door():
    global first_dialog, ExitFromRoom, bookquest, text4,textdenhelp,BigQ,LitQ
    global door_flag
    if 1000-50 < x and x < 1000+50:

        door_flag = keyPress(door_flag)
        if ExitFromRoom == False:
            win.blit(vibr, (x + 100, 600))
            win.blit(ButF, (1030, 230))
            win.blit(text3, (950, 200))
            if door_flag:
                win.blit(PDA, (300, 170))
                first_dialog = True
        if first_dialog == True and PC == False:
            f5 = pygame.font.Font('BK0010.ttf', 35)
            text5 = f5.render('Нужно помочь Денису!', 1, (255, 0, 191))
            win.blit(text5, (930, 270))
            bookquest = True
            # win.blit(citygif[animCount// 5],(0,0))
    elif door_flag == True:
        door_flag = False




# уникальный флаг для переключения состояния
books_flag = False
#Открываем учебник
def books():
    global bookquest, PC,denhX
    global books_flag
    fbook = pygame.font.Font('BK0010.ttf', 35)
    textbook = fbook.render('Открыть учебник', 1, (255, 255, 255))
    if bookquest == True:
        if 50-50 < x and x < 50+50:
            win.blit(textbook,(20, 270))
            win.blit(ButF, (100, 300))
            books_flag = keyPress(books_flag)
            # Вырисовывем планшет
            if books_flag:
                win.blit(book,(0,0))
                PC = True
        elif books_flag:
            books_flag = False


# уникальный флаг для переключения состояния
wind_flag = False
#Посмотреть в окно
def wind():
    global wind_flag
    if x > 350 and x<600:
        win.blit(text2, (483, 380))
        win.blit(ButF, (579, 410))

        wind_flag = keyPress(wind_flag)
        # Вырисовывем планшет
        if wind_flag:
            win.blit(WinWatch,(0,0))
    elif wind_flag:
        wind_flag = False


# уникальный флаг для переключения состояния
comp_flag = False
#Работа с пк
def comp():
    global PC, ExitFromRoom,denquest,BigQ,LitQ
    global comp_flag
    if PC == True:
        if x > 870 and x < 940:
            win.blit(text1, (960, 350))
            win.blit(ButF, (960, 380))
            comp_flag = keyPress(comp_flag)
            if comp_flag:
                win.blit(WinPass, (0, 0))
                ExitFromRoom = True
                BigQ = 'Вот не задача!'
                LitQ = "Мне нужно найти пароль от компьюетра!"
        elif comp_flag:
            comp_flag = False


def posters(x_cords,image):
    if x_cords-30 < x and x < x_cords+30:
        win.blit(ButF, (x_cords+85, 450))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                win.blit(image, (0, 0))


def photo_camera(x_cords):
    if x_cords-30 < x and x < x_cords+30:
        win.blit(ButF, (x_cords+85, 500))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                win.blit(canon, (200, 0))

#переменная работы игры
run = True
while run:
    pygame.display.update()
    clock.tick(25)

    #обновляем игровой цикл каждые 0,05 секунд
    pygame.time.delay(50)
    #Перебераем события игры для выхода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #Назначаем клавиши управления
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>-100:
        x -=speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x<1200-width-15:
        x +=speed
        right = True
        left = False

    else:
        right = False
        left = False
        animCount = 0


    drawWindow()
    if scene == 1:
        change_scene(1000, 2)
        door()
        books()
        wind()
        comp()
    elif scene == 2:
        change_scene(-100, 1)
        posters(0, Poster1)
        posters(350, Poster2)
        posters(700, Poster3)
        photo_camera(800)
        change_scene(1000, 3)
    elif scene == 3:
        change_scene(-100, 2)

    #Обновляем окно
    # win.fill((0,0,0))



