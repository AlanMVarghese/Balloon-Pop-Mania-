import math

import pygame
import random
import HandTrackingModule as htm
import cv2


import mediapipe as mp
# BGM



cap = cv2.VideoCapture(0)
cap.set(3, 800)
cap.set(4, 600)
detector = htm.handDetector(maxHands=1)


pygame.init()


pygame.mixer.music.load("Into-Oblivion.mp3")
pygame.mixer.music.play(-1)


score = 0
font = pygame.font.Font('freesansbold.ttf', 32)


#1530, 800
screen = pygame.display.set_mode((1530, 800), pygame.RESIZABLE)

AimImg = pygame.image.load('aim (1).png')
AimX = 370
AimY = 480
AimX_change = 0


Balloon1Img = pygame.image.load("balloon (1).png")
Balloon1X = random.randrange(50,750)
Balloon1Y = 600
Balloon2Img = pygame.image.load("balloon (2).png")
Balloon2X = random.randrange(50,750)
Balloon2Y = 600
Balloon3Img = pygame.image.load("balloon (3).png")
Balloon3X = random.randrange(50,750)
Balloon3Y = 600
Balloon4Img = pygame.image.load("balloon (5).png")
Balloon4X = random.randrange(50,750)
Balloon4Y = 600
Balloon5Img = pygame.image.load("balloon.png")
Balloon5X = random.randrange(50,750)
Balloon5Y = 600


def show_score(x, y):
    score_value = font.render("Score : " + str(score), True, (0, 0, 0))
    screen.blit(score_value, (x, y))

def Aim(x, y):
    screen.blit(AimImg, (x, y))

def Balloon(BalloonImg, x, y):
    screen.blit(BalloonImg, (x, y))

def isCollision(BalloonX, BalloonY, AimX, AimY):
    distance_shoot = math.sqrt(math.pow(BalloonX + 20 - AimX, 2) + (math.pow(BalloonY + 20 - AimY, 2)))
    if distance_shoot < 50:
        return True
    else:
        return False



running = True
while running:

    success, img = cap.read()

    img = cv2.flip(img, 1)
    img = detector.detectHands(img)



    lmlist = detector.findpos(img)

    if len(lmlist) != 0:

        tip_middle_fingerx = lmlist[12][1]
        tip_middle_fingery = lmlist[12][2]

        bottom_middle_fingerx = lmlist[9][1]
        bottom_middle_fingery = lmlist[9][2]

        distance_fingers = math.sqrt(math.pow(bottom_middle_fingerx-tip_middle_fingerx,2)+ math.pow(bottom_middle_fingery-tip_middle_fingery,2))
        if distance_fingers < 50:
            # look for collision
            collision1 = isCollision(Balloon1X, Balloon1Y, AimX, AimY)
            collision2 = isCollision(Balloon2X, Balloon2Y, AimX, AimY)

            collision3 = isCollision(Balloon3X, Balloon3Y, AimX, AimY)

            collision4 = isCollision(Balloon4X, Balloon4Y, AimX, AimY)
            collision5 = isCollision(Balloon5X, Balloon5Y, AimX, AimY)
            if collision1:

                explosionSound = pygame.mixer.Sound("202230__deraj__pop-sound.wav")
                explosionSound.play()
                score += 1
                print(score)

                Balloon1Y = 700
                Balloon1X = random.randint(75, 725)
            elif collision2:

                explosionSound = pygame.mixer.Sound("202230__deraj__pop-sound.wav")
                explosionSound.play()
                score += 1
                print(score)

                Balloon2Y = 700
                Balloon2X = random.randint(75, 725)
            elif collision3:

                explosionSound = pygame.mixer.Sound("202230__deraj__pop-sound.wav")
                explosionSound.play()
                score += 1
                print(score)

                Balloon3Y = 700
                Balloon3X = random.randint(75, 735)
            elif collision4:

                explosionSound = pygame.mixer.Sound("202230__deraj__pop-sound.wav")
                explosionSound.play()
                score += 1
                print(score)

                Balloon4Y = 700
                Balloon4X = random.randint(75, 745)
            elif collision5:

                explosionSound = pygame.mixer.Sound("202230__deraj__pop-sound.wav")
                explosionSound.play()
                score += 1
                print(score)

                Balloon5Y = 700
                Balloon5X = random.randint(75, 755)



        else:
            AimX = lmlist[9][1] * 2
            AimY = lmlist[9][2] * 2
            #print(AimX,AimY)



    cv2.imshow("Image", img)
    cv2.waitKey(1)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





    # speed of balloon
    Balloon1Y -= 10
    Balloon2Y -= 5
    Balloon3Y -= 2
    Balloon5Y -= 3
    Balloon4Y -= 7


    # respawn balloon at different location if it has gone off screen with random speeds
    if Balloon1Y < -300:
        Balloon1Y = 700
        Balloon1X = random.randint(75,725)
    if Balloon2Y < -300:
        Balloon2Y = 700
        Balloon2X = random.randint(75,725)
    if Balloon3Y < -300:
        Balloon3Y = 700
        Balloon3X = random.randint(75,725)
    if Balloon4Y < -300:
        Balloon4Y = 700
        Balloon4X = random.randint(75,725)
    if Balloon5Y < -300:
        Balloon5Y = 700
        Balloon5X = random.randint(75,725)

    screen.fill((255,255,255))
    Balloon(Balloon1Img, Balloon1X,Balloon1Y)
    Balloon(Balloon2Img, Balloon2X,Balloon2Y)
    Balloon(Balloon3Img, Balloon3X,Balloon3Y)
    Balloon(Balloon4Img, Balloon4X,Balloon4Y)
    Balloon(Balloon5Img, Balloon5X,Balloon5Y)

    Aim(AimX,AimY)
    show_score(10, 10)
    pygame.display.update()