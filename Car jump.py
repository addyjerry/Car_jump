import pygame

import math

from pygame import mixer


pygame.init()
#Window
window=pygame.display.set_mode((800,600))
Title =pygame.display.set_caption('CAR JUMP')
icon =pygame.image.load('accident.png')
pygame.display.set_icon(icon)

backgroundImg=pygame.image.load('forest-road.jpg')

#background music
mixer.music.load('aj.mp3')
mixer.music.play(-1)

#Boy
boyImg=pygame.image.load('boy.png')
boyX=10
boyY=405 
boyX_change=0
boyY_change=0

#function for boy
def boy(x,y):
    window.blit(boyImg,(x,y))

#Collision function
def isCollision(boyX,boyY,policeX,policeY,carX,carY):
    distance_A=math.sqrt((math.pow(policeX-boyX,2)) +(math.pow(policeY-boyY,2)))
    distance_B=math.sqrt((math.pow(carX-boyX,2))+ (math.pow(carY-boyY,2)))
    if distance_A <25 or distance_B <25:
        gameover(gameX,gameY)
    


#Score
score_value =0
font =pygame.font.Font('freesansbold.ttf',34)
textX =10
textY =10

#function for score
def score(x,y):
    score =font.render("Score :" + str(score_value),True,(0,0,0))
    window.blit(score,(x,y))

#gameover

font =pygame.font.Font('freesansbold.ttf',50)
gameX =400
gameY =300

#function for gameover
def gameover(x,y):
    gameover =font.render('GAME OVER' ,True, (255,0,0))
    window.blit(gameover,(x,y))

#Car
carImg =pygame.image.load('car.png')
carX =700
carY =425
carX_change=0
carY_change=0

#function for car
def car(x,y):
    window.blit(carImg,(x,y))

#Police
policeImg =pygame.image.load('police.png')
policeX =500
policeY =415
policeX_change=0
policeY_change=0.1

#function for police
def police(x,y):
    window.blit(policeImg,(x,y))

    

#To keep game running
running = True
while running:
    window.fill((0,0,0))


    window.blit(backgroundImg,(0,0))
   

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running =False


        #How to move player
        if event.type ==pygame.KEYDOWN and boyY >=405:
            if event.key == pygame.K_SPACE:
                boyY_change=-0.8

            if event.key==pygame.K_RIGHT:
                boyX_change=0.5
            if event.key ==pygame.K_LEFT:
                boyX_change=-0.5
            

        if event.type ==pygame.KEYUP:
            if event.key==pygame.K_SPACE or pygame.K_RIGHT:
                boyY_change=0.5
                boyX_change=0

        #Police car movement
    policeX_change = -0.3
    if policeX< -100:
        policeX=810
        score_value+=1 
        Carhorn=mixer.Sound('horn.wav')
        Carhorn.play()                       

    #Car movement
    carX_change =-0.3
    if carX< -100:
        carX=810
        score_value +=1
        Carhorn=mixer.Sound('horn.wav')
        Carhorn.play(3)

    #Score
    score(textX,textY)
     

    #boy
    if boyY >=405:
        boyY=405
    if boyY <=250:
        boyY =250
    
    #collision
    collision =isCollision(boyX,boyY,policeX,policeY,carX,carY)
 
    if collision:
        window.fill(255,255,255)
        gameover(gameX,gameY)

    boyX +=boyX_change
    boyY +=boyY_change
    boy(boyX,boyY)

    #Calling car
    carX +=carX_change
    car(carX,carY)

    #Calling police
    policeX +=policeX_change
    police(policeX,policeY)
 
    pygame.display.update()