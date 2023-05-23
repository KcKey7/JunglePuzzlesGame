#Import Modules
import pygame
import sys
import os
import math

#Initializing Constructor
pygame.init()

#Set World Values
worldx = 900
worldy = 900
fps = 100
ani = 4

#Set other Variables
page = 1
levelAvailability = 1
isPaused = False
isWin = False
isDeath = False
world = pygame.display.set_mode([worldx, worldy])

#Set Color Values
BLACK = (0, 0, 0)
ALPHA = (0, 255, 0)
WHITE = (255, 255, 255)
YELLOW = (240, 230, 140)
D_YELLOW =(203,185,26)

#Set Fonts
titleFont = pygame.font.Font("Fonts/titleFont.ttf", 150)
titleFontBackground = pygame.font.Font("Fonts/titleFontBackground.ttf", 150)
titleFontOutline = pygame.font.Font("Fonts/titleFontOutline.ttf", 150)

#Title Background
title_bg_img = pygame.image.load("Backgrounds/titleBackground.png")
title_bg_img = pygame.transform.scale(title_bg_img,(worldx, worldy))

#Title
titleBackground1 = titleFontBackground.render("Jungle", True, WHITE)
title1 = titleFont.render("Jungle", True, YELLOW)
titleOutline1 = titleFontOutline.render("Jungle", True, D_YELLOW)
titleBackground2 = titleFontBackground.render("Puzzles", True, WHITE)
title2 = titleFont.render("Puzzles", True, YELLOW)
titleOutline2 = titleFontOutline.render("Puzzles", True, D_YELLOW)

#Quit Button
quitx = 380
quitSize = 75

#Level Page Button
levelsx = 360
levelSize = 75

#Back To Title Button
titleBackx = 1
titleBackSize = 75

#Level Page Background
levels_page_bg_img = pygame.image.load("Backgrounds/levelsBackground.png")
levels_page_bg_img = pygame.transform.scale(levels_page_bg_img,(worldx, worldy))

#Level Button images
unavailableButton = pygame.image.load("Buttons/unavailableLevelButton.png")

darkButton1 = pygame.image.load("Buttons/darkButton1.png")
lightButton1 = pygame.image.load("Buttons/lightButton1.png")

darkButton2 = pygame.image.load("Buttons/darkButton2.png")
lightButton2 = pygame.image.load("Buttons/lightButton2.png")

darkButton3 = pygame.image.load("Buttons/darkButton3.png")
lightButton3 = pygame.image.load("Buttons/lightButton3.png")

darkButton4 = pygame.image.load("Buttons/darkButton4.png")
lightButton4 = pygame.image.load("Buttons/lightButton4.png")

darkButton5 = pygame.image.load("Buttons/darkButton5.png")
lightButton5 = pygame.image.load("Buttons/lightButton5.png")

darkButton6 = pygame.image.load("Buttons/darkButton6.png")
lightButton6 = pygame.image.load("Buttons/lightButton6.png")

darkButton7 = pygame.image.load("Buttons/darkButton7.png")
lightButton7 = pygame.image.load("Buttons/lightButton7.png")

darkButton8 = pygame.image.load("Buttons/darkButton8.png")
lightButton8 = pygame.image.load("Buttons/lightButton8.png")

darkButton9 = pygame.image.load("Buttons/darkButton9.png")
lightButton9 = pygame.image.load("Buttons/lightButton9.png")

darkButton10 = pygame.image.load("Buttons/darkButton10.png")
lightButton10 = pygame.image.load("Buttons/lightButton10.png")

darkButton11 = pygame.image.load("Buttons/darkButton11.png")
lightButton11 = pygame.image.load("Buttons/lightButton11.png")

darkButton12 = pygame.image.load("Buttons/darkButton12.png")
lightButton12 = pygame.image.load("Buttons/lightButton12.png")

darkButton13 = pygame.image.load("Buttons/darkButton13.png")
lightButton13 = pygame.image.load("Buttons/lightButton13.png")

darkButton14 = pygame.image.load("Buttons/darkButton14.png")
lightButton14 = pygame.image.load("Buttons/lightButton14.png")

darkButton15 = pygame.image.load("Buttons/darkButton15.png")
lightButton15 = pygame.image.load("Buttons/lightButton15.png")

darkButton16 = pygame.image.load("Buttons/darkButton16.png")
lightButton16 = pygame.image.load("Buttons/lightButton16.png")

darkButton17 = pygame.image.load("Buttons/darkButton17.png")
lightButton17 = pygame.image.load("Buttons/lightButton17.png")

darkButton18 = pygame.image.load("Buttons/darkButton18.png")
lightButton18 = pygame.image.load("Buttons/lightButton18.png")

darkButton19 = pygame.image.load("Buttons/darkButton19.png")
lightButton19 = pygame.image.load("Buttons/lightButton19.png")

darkButton20 = pygame.image.load("Buttons/darkButton20.png")
lightButton20 = pygame.image.load("Buttons/lightButton20.png")

darkButton21 = pygame.image.load("Buttons/darkButton21.png")
lightButton21 = pygame.image.load("Buttons/lightButton21.png")

darkButton22 = pygame.image.load("Buttons/darkButton22.png")
lightButton22 = pygame.image.load("Buttons/lightButton22.png")

darkButton23 = pygame.image.load("Buttons/darkButton23.png")
lightButton23 = pygame.image.load("Buttons/lightButton23.png")

darkButton24 = pygame.image.load("Buttons/darkButton24.png")
lightButton24 = pygame.image.load("Buttons/lightButton24.png")

darkButton25 = pygame.image.load("Buttons/darkButton25.png")
lightButton25 = pygame.image.load("Buttons/lightButton25.png")


#Level Buttons
def levelButtonIMG(level, xParameter1, xParameter2, yParameter1, yParameter2, buttonx, buttony, darkButton, lightButton):
    if levelAvailability >= level:
        if xParameter1 <= mouse[0]  <= xParameter2 and yParameter1 <= mouse[1] <= yParameter2:
            world.blit(lightButton, (buttonx, buttony))
        else:
            world.blit(darkButton, (buttonx, buttony))
    else:
            world.blit(unavailableButton, (buttonx, buttony))

#Inside Level Background
levels_bg_img = pygame.image.load("Backgrounds/insideLevelsBackground.jpg")

#Pause Menu
def pauseButtonIMG():
    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
        pauseButtonSize = 60
        pauseButtonx = 50
    else:
        pauseButtonSize = 50
        pauseButtonx = 50

    pauseButtonFont = pygame.font.Font("Fonts/titleFont.ttf", pauseButtonSize)
    pauseButtonBackgroundFont = pygame.font.Font("Fonts/titleFontBackground.ttf", pauseButtonSize)
    pauseButtonOutlineFont = pygame.font.Font("Fonts/titleFontOutline.ttf", pauseButtonSize)
    pauseButton = pauseButtonFont.render("Pause", True, YELLOW)
    pauseButtonBackground = pauseButtonBackgroundFont.render("Pause", True, WHITE)
    pauseButtonOutline = pauseButtonOutlineFont.render("Pause", True, D_YELLOW)
    world.blit(pauseButtonBackground, (pauseButtonx, 50))
    world.blit(pauseButton, (pauseButtonx, 50))
    world.blit(pauseButtonOutline, (pauseButtonx, 50))

#Set Pause Popup images/fonts
pausePopupIMG = pygame.image.load("popups/popupBoard.png")

pausedFont = pygame.font.Font("Fonts/titleFont.ttf", 125)
pausedFontBackground = pygame.font.Font("Fonts/titleFontBackground.ttf", 125)
pausedFontOutline = pygame.font.Font("Fonts/titleFontOutline.ttf", 125)

pausedBackground = pausedFontBackground.render("Paused", True, WHITE)
paused = pausedFont.render("Paused", True, YELLOW)
pausedOutline = pausedFontOutline.render("Paused", True, D_YELLOW)

def pausePopup():
    world.blit(pausePopupIMG, (75, 75))

    world.blit(pausedBackground, (290, 265))
    world.blit(paused, (290, 265))
    world.blit(pausedOutline, (290, 265))

    #Back to Menu
    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
        BacktoLevelsButtonSize = 75
        BacktoLevelsButtonx = 250
    else:
        BacktoLevelsButtonSize = 65
        BacktoLevelsButtonx = 275

    pauseButtonFont = pygame.font.Font("Fonts/titleFont.ttf", BacktoLevelsButtonSize)
    pauseButtonBackgroundFont = pygame.font.Font("Fonts/titleFontBackground.ttf", BacktoLevelsButtonSize)
    pauseButtonOutlineFont = pygame.font.Font("Fonts/titleFontOutline.ttf", BacktoLevelsButtonSize)
    pauseButton = pauseButtonFont.render("Back To Menu", True, YELLOW)
    pauseButtonBackground = pauseButtonBackgroundFont.render("Back To Menu", True, WHITE)
    pauseButtonOutline = pauseButtonOutlineFont.render("Back To Menu", True, D_YELLOW)
    world.blit(pauseButtonBackground, (BacktoLevelsButtonx, 400))
    world.blit(pauseButton, (BacktoLevelsButtonx, 400))
    world.blit(pauseButtonOutline, (BacktoLevelsButtonx, 400))
    #Continue
    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
        continueButtonSize = 75
        continueButtonx = 310
    else:
        continueButtonSize = 65
        continueButtonx = 335

    pauseButtonFont = pygame.font.Font("Fonts/titleFont.ttf", continueButtonSize)
    pauseButtonBackgroundFont = pygame.font.Font("Fonts/titleFontBackground.ttf", continueButtonSize)
    pauseButtonOutlineFont = pygame.font.Font("Fonts/titleFontOutline.ttf", continueButtonSize)
    pauseButton = pauseButtonFont.render("Continue", True, YELLOW)
    pauseButtonBackground = pauseButtonBackgroundFont.render("Continue", True, WHITE)
    pauseButtonOutline = pauseButtonOutlineFont.render("Continue", True, D_YELLOW)
    world.blit(pauseButtonBackground, (continueButtonx, 475))
    world.blit(pauseButton, (continueButtonx, 475))
    world.blit(pauseButtonOutline, (continueButtonx, 475))

    #Quit Game
    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
        QuitButtonSize = 75
        QuitButtonx = 300
    else:
        QuitButtonSize = 65
        QuitButtonx = 325

    pauseButtonFont = pygame.font.Font("Fonts/titleFont.ttf", QuitButtonSize)
    pauseButtonBackgroundFont = pygame.font.Font("Fonts/titleFontBackground.ttf", QuitButtonSize)
    pauseButtonOutlineFont = pygame.font.Font("Fonts/titleFontOutline.ttf", QuitButtonSize)
    pauseButton = pauseButtonFont.render("Quit game", True, YELLOW)
    pauseButtonBackground = pauseButtonBackgroundFont.render("Quit game", True, WHITE)
    pauseButtonOutline = pauseButtonOutlineFont.render("Quit game", True, D_YELLOW)
    world.blit(pauseButtonBackground, (QuitButtonx, 550))
    world.blit(pauseButton, (QuitButtonx, 550))
    world.blit(pauseButtonOutline, (QuitButtonx, 550))

#Set Win Popup images/fonts
winPopupIMG = pygame.image.load("popups/popupBoard.png")

winFont = pygame.font.Font("Fonts/titleFont.ttf", 125)
winFontBackground = pygame.font.Font("Fonts/titleFontBackground.ttf", 125)
winFontOutline = pygame.font.Font("Fonts/titleFontOutline.ttf", 125)

winBackground = winFontBackground.render("You Win!", True, WHITE)
win = winFont.render("You Win!", True, YELLOW)
winOutline = winFontOutline.render("You Win!", True, D_YELLOW)

def winPopup():
    world.blit(winPopupIMG, (75, 75))

    world.blit(winBackground, (245, 265))
    world.blit(win, (245, 265))
    world.blit(winOutline, (245, 265))

    #Back to Menu
    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
        BacktoLevelsButtonSize = 75
        BacktoLevelsButtonx = 250
    else:
        BacktoLevelsButtonSize = 65
        BacktoLevelsButtonx = 275

    pauseButtonFont = pygame.font.Font("Fonts/titleFont.ttf", BacktoLevelsButtonSize)
    pauseButtonBackgroundFont = pygame.font.Font("Fonts/titleFontBackground.ttf", BacktoLevelsButtonSize)
    pauseButtonOutlineFont = pygame.font.Font("Fonts/titleFontOutline.ttf", BacktoLevelsButtonSize)
    pauseButton = pauseButtonFont.render("Back To Menu", True, YELLOW)
    pauseButtonBackground = pauseButtonBackgroundFont.render("Back To Menu", True, WHITE)
    pauseButtonOutline = pauseButtonOutlineFont.render("Back To Menu", True, D_YELLOW)
    world.blit(pauseButtonBackground, (BacktoLevelsButtonx, 400))
    world.blit(pauseButton, (BacktoLevelsButtonx, 400))
    world.blit(pauseButtonOutline, (BacktoLevelsButtonx, 400))
    #Replay Level
    if 275 <= mouse[0] <= 575 and 475 <= mouse[1] <= 515:
        replayButtonSize = 75
        replayButtonx = 300
    else:
        replayButtonSize = 65
        replayButtonx = 325

    pauseButtonFont = pygame.font.Font("Fonts/titleFont.ttf", replayButtonSize)
    pauseButtonBackgroundFont = pygame.font.Font("Fonts/titleFontBackground.ttf", replayButtonSize)
    pauseButtonOutlineFont = pygame.font.Font("Fonts/titleFontOutline.ttf", replayButtonSize)
    pauseButton = pauseButtonFont.render("Next Level", True, YELLOW)
    pauseButtonBackground = pauseButtonBackgroundFont.render("Next Level", True, WHITE)
    pauseButtonOutline = pauseButtonOutlineFont.render("Next Level", True, D_YELLOW)
    world.blit(pauseButtonBackground, (replayButtonx, 475))
    world.blit(pauseButton, (replayButtonx, 475))
    world.blit(pauseButtonOutline, (replayButtonx, 475))

    #Quit Game
    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
        QuitButtonSize = 75
        QuitButtonx = 300
    else:
        QuitButtonSize = 65
        QuitButtonx = 325

    pauseButtonFont = pygame.font.Font("Fonts/titleFont.ttf", QuitButtonSize)
    pauseButtonBackgroundFont = pygame.font.Font("Fonts/titleFontBackground.ttf", QuitButtonSize)
    pauseButtonOutlineFont = pygame.font.Font("Fonts/titleFontOutline.ttf", QuitButtonSize)
    pauseButton = pauseButtonFont.render("Quit game", True, YELLOW)
    pauseButtonBackground = pauseButtonBackgroundFont.render("Quit game", True, WHITE)
    pauseButtonOutline = pauseButtonOutlineFont.render("Quit game", True, D_YELLOW)
    world.blit(pauseButtonBackground, (QuitButtonx, 550))
    world.blit(pauseButton, (QuitButtonx, 550))
    world.blit(pauseButtonOutline, (QuitButtonx, 550))

#Set Lose Popup images/fonts
losePopupIMG = pygame.image.load("popups/popupBoard.png")

loseFont = pygame.font.Font("Fonts/titleFont.ttf", 125)
loseFontBackground = pygame.font.Font("Fonts/titleFontBackground.ttf", 125)
loseFontOutline = pygame.font.Font("Fonts/titleFontOutline.ttf", 125)

loseBackground = loseFontBackground.render("You Died!", True, WHITE)
lose = loseFont.render("You Died!", True, YELLOW)
loseOutline = loseFontOutline.render("You Died!", True, D_YELLOW)

def losePopup():
    world.blit(losePopupIMG, (75, 75))

    world.blit(loseBackground, (230, 265))
    world.blit(lose, (230, 265))
    world.blit(loseOutline, (230, 265))

    #Back to Menu
    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
        BacktoLevelsButtonSize = 75
        BacktoLevelsButtonx = 250
    else:
        BacktoLevelsButtonSize = 65
        BacktoLevelsButtonx = 275

    pauseButtonFont = pygame.font.Font("Fonts/titleFont.ttf", BacktoLevelsButtonSize)
    pauseButtonBackgroundFont = pygame.font.Font("Fonts/titleFontBackground.ttf", BacktoLevelsButtonSize)
    pauseButtonOutlineFont = pygame.font.Font("Fonts/titleFontOutline.ttf", BacktoLevelsButtonSize)
    pauseButton = pauseButtonFont.render("Back To Menu", True, YELLOW)
    pauseButtonBackground = pauseButtonBackgroundFont.render("Back To Menu", True, WHITE)
    pauseButtonOutline = pauseButtonOutlineFont.render("Back To Menu", True, D_YELLOW)
    world.blit(pauseButtonBackground, (BacktoLevelsButtonx, 400))
    world.blit(pauseButton, (BacktoLevelsButtonx, 400))
    world.blit(pauseButtonOutline, (BacktoLevelsButtonx, 400))

    #Quit Game
    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
        QuitButtonSize = 75
        QuitButtonx = 300
    else:
        QuitButtonSize = 65
        QuitButtonx = 325

    pauseButtonFont = pygame.font.Font("Fonts/titleFont.ttf", QuitButtonSize)
    pauseButtonBackgroundFont = pygame.font.Font("Fonts/titleFontBackground.ttf", QuitButtonSize)
    pauseButtonOutlineFont = pygame.font.Font("Fonts/titleFontOutline.ttf", QuitButtonSize)
    pauseButton = pauseButtonFont.render("Quit game", True, YELLOW)
    pauseButtonBackground = pauseButtonBackgroundFont.render("Quit game", True, WHITE)
    pauseButtonOutline = pauseButtonOutlineFont.render("Quit game", True, D_YELLOW)
    world.blit(pauseButtonBackground, (QuitButtonx, 475))
    world.blit(pauseButton, (QuitButtonx, 475))
    world.blit(pauseButtonOutline, (QuitButtonx, 475))

#Platforms
class Platform(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Platforms/platform.png")
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

class Platform2(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Platforms/platform2.png")
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

class Platform3(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Platforms/platform3.png")
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

class Platform4(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Platforms/platform4.png")
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

class Platform5(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Platforms/platform5.png")
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

class Platform6(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Platforms/platform6.png")
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

class Platform7(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Platforms/platform7.png")
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

class Platform8(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Platforms/platform8.png")
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

class Door(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Platforms/door.png")
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

#Coins
class Coin(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, imgw, imgh, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Coin.png")
        self.image.convert_alpha()
        self.image.set_colorkey(ALPHA)
        self.rect = self.image.get_rect()
        self.rect.y = yloc
        self.rect.x = xloc

#User
playerimg = pygame.image.load("Character.png")
playerX = 40
playerY = 775
playerX_change = 0
playerY_change = 0

isJump = False
v = 7
m = 1

def player(x,y):
    world.blit(playerimg, (x,y))

#Levels
class Level():
    def ground(lvl, gloc, tx, ty):
        ground_list = pygame.sprite.Group()
        i = 0
        if lvl == 1:
            while i < len(gloc):
                ground = Platform(gloc[i], worldy - ty, tx, ty, "Platforms/platform.png")
                ground_list.add(ground)
                i = i + 1
   
        if lvl == 2:
            print("Level " + str(lvl))
   
        return ground_list


    def platform(lvl):
        plat_list = pygame.sprite.Group()
        #Level 1
        if lvl == 1:
            plat = Platform3(110, worldy-45-88, 5, 6,'Platforms/platform3.png')
            plat_list.add(plat)
            plat = Platform2(240, worldy-75-78, 5, 6,'Platforms/platform2.png')
            plat_list.add(plat)
            plat = Platform3(455, worldy-85-85, 5, 6,'Platforms/platform3.png')
            plat_list.add(plat)
            plat = Platform4(580, worldy-100-100, 5, 6,'Platforms/platform4.png')
            plat_list.add(plat)
            plat = Platform6(495, worldy-180-210, 5, 6,'Platforms/platform6.png')
            plat_list.add(plat)
            plat = Platform5(670, worldy-130-120, 5, 6,'Platforms/platform5.png')
            plat_list.add(plat)
            plat = Platform2(290, worldy-200-220, 5, 6,'Platforms/platform2.png')
            plat_list.add(plat)
            plat = Platform7(70, worldy-220-250, 5, 6,'Platforms/platform7.png')
            plat_list.add(plat)
            plat = Platform8(250, worldy-290-330, 5, 6,'Platforms/platform8.png')
            plat_list.add(plat)
            plat = Platform5(150, worldy-320-350, 5, 6,'Platforms/platform5.png')
            plat_list.add(plat)
            plat = Platform7(290, worldy-350-390, 5, 6,'Platforms/platform7.png')
            plat_list.add(plat)
            plat = Door(330, worldy-355-485, 5, 6,'platforms/door.png')
            plat_list.add(plat)
        if lvl == 2:
            print("Level" + str(lvl))


        return plat_list

    def coin(lvl):
        coin_list = pygame.sprite.Group()
        if lvl == 1:
            coin = Coin(190, worldy-250-290, 5, 6, "Coin.png")
            coin_list.add(coin)
            coin = Coin(690, worldy-150-190, 5, 6, "Coin.png")
            coin_list.add(coin)
        if lvl == 2:
            print("Level" + str(lvl))

        return coin_list

gloc = []
tx = 150
ty = 50


i = 0
while i <= (worldx/tx) + tx:
    gloc.append(i*tx)
    i = i + 1

ground_list = Level.ground(1, gloc, tx, ty)
plat_list = Level.platform(1)
coin_list = Level.coin(1)

#Setup(Goes right before main loop)
clock = pygame.time.Clock()
backdropbox = world.get_rect()
main = True

#Main loop(Has to go at end of code)
while main:
    #Quit Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
    mouse = pygame.mouse.get_pos()


    #title page
    if page == 1:
        #draw title
        world.blit(title_bg_img, backdropbox)
        world.blit(titleBackground1, (255, 100))
        world.blit(title1, (255, 100))
        world.blit(titleOutline1, (255, 100))
        world.blit(titleBackground2, (225, 225))
        world.blit(title2, (225, 225))
        world.blit(titleOutline2, (225, 225))


        #Quit Button
        if 380 <= mouse[0] <= 500 and 350 <= mouse[1] <= 390:
            quitSize = 100
            quitx = 365
        else:
            quitSize = 75
            quitx = 380


        quitFont = pygame.font.Font("Fonts/titleFont.ttf", quitSize)
        quitFontBackground = pygame.font.Font("Fonts/titleFontBackground.ttf", quitSize)
        quitFontOutline = pygame.font.Font("Fonts/titleFontOutline.ttf", quitSize)
        quit = quitFont.render("Quit", True, YELLOW)
        quitBackground = quitFontBackground.render("Quit", True, WHITE)
        quitOutline = quitFontOutline.render("Quit", True, D_YELLOW)
        world.blit(quitBackground, (quitx, 350))
        world.blit(quit, (quitx, 350))
        world.blit(quitOutline, (quitx, 350))


    #Level Page Button
        if 360 <= mouse[0] <= 480 and 450 <= mouse[1] <= 490:
            levelSize = 100
            levelsx = 340
        else:
            levelSize = 75
            levelsx = 360
        if event.type == pygame.MOUSEBUTTONDOWN:
                if 375 <= mouse[0] <= 500 and 350 <= mouse[1] <= 390:
                    pygame.quit()
                if 360 <= mouse[0] <= 480 and 450 <= mouse[1] <= 490:
                        page = 2
   
        levelsFont = pygame.font.Font("Fonts/titleFont.ttf", levelSize)
        levelsFontBackground = pygame.font.Font("Fonts/titleFontBackground.ttf", levelSize)
        levelsFontOutline = pygame.font.Font("Fonts/titleFontOutline.ttf", levelSize)
        levelsButton = levelsFont.render("Levels", True, YELLOW)
        levelsButtonBackground = levelsFontBackground.render("Levels", True, WHITE)
        levelsButtonOutline = levelsFontOutline.render("Levels", True, D_YELLOW)
        world.blit(levelsButtonBackground, (levelsx, 450))
        world.blit(levelsButton, (levelsx, 450))
        world.blit(levelsButtonOutline, (levelsx, 450))
   
    #level Menu Page
    elif page == 2:
        #Back Button Image
        world.blit(levels_page_bg_img, backdropbox)
        if 170 <= mouse[0] <= 270 and 170 <= mouse[1] <= 210:
            titleBackSize = 60
            titleBackx = 170
        else:
            titleBackSize = 50
            titleBackx = 175


        #Level Button Availability and Images
        levelButtonIMG(1, 210, 270, 225, 285, 200, 215, darkButton1, lightButton1)

        levelButtonIMG(2, 310, 370, 225, 285, 300, 215, darkButton2, lightButton2)
       
        levelButtonIMG(3, 410, 470, 225, 285, 400, 215, darkButton3, lightButton3)

        levelButtonIMG(4, 510, 570, 225, 285, 500, 215, darkButton4, lightButton4)

        levelButtonIMG(5, 610, 670, 225, 285, 600, 215, darkButton5, lightButton5)

        levelButtonIMG(6, 210, 270, 325, 385, 200, 315, darkButton6, lightButton6)

        levelButtonIMG(7, 310, 370, 325, 385, 300, 315, darkButton7, lightButton7)

        levelButtonIMG(8, 410, 470, 325, 385, 400, 315, darkButton8, lightButton8)

        levelButtonIMG(9, 510, 570, 325, 385, 500, 315, darkButton9, lightButton9)

        levelButtonIMG(10, 610, 670, 325, 385, 600, 315, darkButton10, lightButton10)

        levelButtonIMG(11, 210, 270, 425, 485, 200, 415, darkButton11, lightButton11)

        levelButtonIMG(12, 310, 370, 425, 485, 300, 415, darkButton12, lightButton12)
       
        levelButtonIMG(13, 410, 470, 425, 485, 400, 415, darkButton13, lightButton13)
       
        levelButtonIMG(14, 510, 570, 425, 485, 500, 415, darkButton14, lightButton14)
       
        levelButtonIMG(15, 610, 670, 425, 485, 600, 415, darkButton15, lightButton15)
       
        levelButtonIMG(16, 210, 270, 525, 585, 200, 515, darkButton16, lightButton16)
       
        levelButtonIMG(17, 310, 370, 525, 585, 300, 515, darkButton17, lightButton17)
       
        levelButtonIMG(18, 410, 470, 525, 585, 400, 515, darkButton18, lightButton18)
       
        levelButtonIMG(19, 510, 570, 525, 585, 500, 515, darkButton19, lightButton19)
       
        levelButtonIMG(20, 610, 670, 525, 585, 600, 515, darkButton20, lightButton20)
       
        levelButtonIMG(21, 210, 270, 625, 685, 200, 615, darkButton21, lightButton21)
       
        levelButtonIMG(22, 310, 370, 625, 685, 300, 615, darkButton22, lightButton22)
       
        levelButtonIMG(23, 410, 470, 625, 685, 400, 615, darkButton23, lightButton23)
       
        levelButtonIMG(24, 510, 570, 625, 685, 500, 615, darkButton24, lightButton24)
       
        levelButtonIMG(25, 610, 670, 625, 685, 600, 615, darkButton25, lightButton25)
       
        #Working Buttons
        if event.type == pygame.MOUSEBUTTONDOWN:
                #Back to menu
                if 170 <= mouse[0] <= 270 and 170 <= mouse[1] <= 210:
                    page = 1
                #Levels
                if 210 <= mouse[0] <= 270 and 225 <= mouse[1] <= 285 and levelAvailability >= 1:
                    page = 3
                    playingLevel = 1
                if 310 <= mouse[0] <= 370 and 225 <= mouse[1] <= 285 and levelAvailability >= 2:
                    page = 3
                    playingLevel = 2
                if 410 <= mouse[0] <= 470 and 225 <= mouse[1] <= 285 and levelAvailability >= 3:
                    page = 3
                    playingLevel = 3
                if 510 <= mouse[0] <= 570 and 225 <= mouse[1] <= 285 and levelAvailability >= 4:
                    page = 3
                    playingLevel = 4
                if 610 <= mouse[0] <= 670 and 225 <= mouse[1] <= 285 and levelAvailability >= 5:
                    page = 3
                    playingLevel = 5
                if 210 <= mouse[0] <= 270 and 325 <= mouse[1] <= 385 and levelAvailability >= 6:
                    page = 3
                    playingLevel = 6
                if 310 <= mouse[0] <= 370 and 325 <= mouse[1] <= 385 and levelAvailability >= 7:
                    page = 3
                    playingLevel = 7
                if 410 <= mouse[0] <= 470 and 325 <= mouse[1] <= 385 and levelAvailability >= 8:
                    page = 3
                    playingLevel = 8
                if 510 <= mouse[0] <= 570 and 325 <= mouse[1] <= 385 and levelAvailability >= 9:
                    page = 3
                    playingLevel = 9
                if 610 <= mouse[0] <= 670 and 325 <= mouse[1] <= 385 and levelAvailability >= 10:
                    page = 3
                    playingLevel = 10
                if 210 <= mouse[0] <= 270 and 425 <= mouse[1] <= 485 and levelAvailability >= 11:
                    page = 3
                    playingLevel = 11
                if 310 <= mouse[0] <= 370 and 425 <= mouse[1] <= 485 and levelAvailability >= 12:
                    page = 3
                    playingLevel = 12
                if 410 <= mouse[0] <= 470 and 425 <= mouse[1] <= 485 and levelAvailability >= 13:
                    page = 3
                    playingLevel = 13
                if 510 <= mouse[0] <= 570 and 425 <= mouse[1] <= 485 and levelAvailability >= 14:
                    page = 3
                    playingLevel = 14
                if 610 <= mouse[0] <= 670 and 425 <= mouse[1] <= 485 and levelAvailability >= 15:
                    page = 3
                    playingLevel = 15
                if 210 <= mouse[0] <= 270 and 525 <= mouse[1] <= 585 and levelAvailability >= 16:
                    page = 3
                    playingLevel = 16
                if 310 <= mouse[0] <= 370 and 525 <= mouse[1] <= 585 and levelAvailability >= 17:
                    page = 3
                    playingLevel = 17
                if 410 <= mouse[0] <= 470 and 525 <= mouse[1] <= 585 and levelAvailability >= 18:
                    page = 3
                    playingLevel = 18
                if 510 <= mouse[0] <= 570 and 525 <= mouse[1] <= 585 and levelAvailability >= 19:
                    page = 3
                    playingLevel = 19
                if 610 <= mouse[0] <= 670 and 525 <= mouse[1] <= 585 and levelAvailability >= 20:
                    page = 3
                    playingLevel = 20
                if 210 <= mouse[0] <= 270 and 625 <= mouse[1] <= 685 and levelAvailability >= 21:
                    page = 3
                    playingLevel = 21
                if 310 <= mouse[0] <= 370 and 625 <= mouse[1] <= 685 and levelAvailability >= 22:
                    page = 3
                    playingLevel = 22
                if 410 <= mouse[0] <= 470 and 625 <= mouse[1] <= 685 and levelAvailability >= 23:
                    page = 3
                    playingLevel = 23
                if 510 <= mouse[0] <= 570 and 625 <= mouse[1] <= 685 and levelAvailability >= 24:
                    page = 3
                    playingLevel = 24
                if 610 <= mouse[0] <= 670 and 625 <= mouse[1] <= 685 and levelAvailability >= 25:
                    page = 3
                    playingLevel = 25

        #Temporary Level Availability Switcher
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                levelAvailability += 1
        
        #Drawing Button
        titleBackFont = pygame.font.Font("Fonts/titleFont.ttf", titleBackSize)
        titleBackBackground = pygame.font.Font("Fonts/titleFontBackground.ttf", titleBackSize)
        titleBackOutline = pygame.font.Font("Fonts/titleFontOutline.ttf", titleBackSize)
        titleBackButton = titleBackFont.render("Back", True, YELLOW)
        titleBackButtonBackground = titleBackBackground.render("Back", True, WHITE)
        titleBackButtonOutline = titleBackOutline.render("Back", True, D_YELLOW)
        world.blit(titleBackButtonBackground, (titleBackx, 170))
        world.blit(titleBackButton, (titleBackx, 170))
        world.blit(titleBackButtonOutline, (titleBackx, 170))


    #Levels   
    elif page == 3:
        #level 1
        if playingLevel == 1:
            world.blit(levels_bg_img, backdropbox)
            ground_list.draw(world)
            plat_list.draw(world)
            coin_list.draw(world)
            player(playerX, playerY)

            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        playerX_change = -2.5
                    if event.key == pygame.K_a:
                        playerX_change = -2.5
                    if event.key == pygame.K_RIGHT: 
                        playerX_change = 2.5
                    if event.key == pygame.K_d:
                        playerX_change = 2.5
                    if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
                        if isJump == False:
                            isJump = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w:
                        playerX_change = 0
                
                playerX += playerX_change
                if isJump:
                    F =(1 / 2)*m*(v**2)
                    playerY -= F
                    v = v-0.5

                    if v < 0:
                        m = -1

                    if v == -7.5:
                        isJump = False
                        v = 7
                        m = 1

                if playerX <= 0:
                    playerX = 0
                elif playerX >= 800:
                    playerX = 800
                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win/Lose Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 2:
                    levelAvailability = 2
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 2
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False
            
            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 2
        elif playingLevel == 2:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 3:
                    levelAvailability = 3
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 3
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 3
        elif playingLevel == 3:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 4:
                    levelAvailability = 4
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 4
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 4
        elif playingLevel == 4:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 5:
                    levelAvailability = 5
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 5
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 5
        elif playingLevel == 5:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 6:
                    levelAvailability = 6
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 6
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 6
        elif playingLevel == 6:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPause = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 7:
                    levelAvailability = 7
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 7
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 7
        elif playingLevel == 7:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 8:
                    levelAvailability = 8
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 8
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 8
        elif playingLevel == 8:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 9:
                    levelAvailability = 9
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 9
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 9
        elif playingLevel == 9:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 10:
                    levelAvailability = 10
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 10
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 10
        elif playingLevel == 10:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 11:
                    levelAvailability = 11
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 11
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 11
        elif playingLevel == 11:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 12:
                    levelAvailability = 12
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 12
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 12
        elif playingLevel == 12:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 13:
                    levelAvailability = 13
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 13
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 13
        elif playingLevel == 13:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 14:
                    levelAvailability = 14
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 14
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 14
        elif playingLevel == 14:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 15:
                    levelAvailability = 15
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 15
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 15
        elif playingLevel == 15:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 16:
                    levelAvailability = 16
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 16
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 16
        elif playingLevel == 16:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 17:
                    levelAvailability = 17
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 17
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 17
        elif playingLevel == 17:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 18:
                    levelAvailability = 18
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 18
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 18
        elif playingLevel == 18:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 19:
                    levelAvailability = 19
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 19
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 19
        elif playingLevel == 19:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 20:
                    levelAvailability = 20
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 20
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 20
        elif playingLevel == 20:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 21:
                    levelAvailability = 21
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 21
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 21
        elif playingLevel == 21:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 22:
                    levelAvailability = 22
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 22
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 22
        elif playingLevel == 22:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 23:
                    levelAvailability = 23
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 23
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 23
        elif playingLevel == 23:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 24:
                    levelAvailability = 24
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 24
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 24
        elif playingLevel == 24:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if levelAvailability < 25:
                    levelAvailability = 25
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 25
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
        #Level 25
        elif playingLevel == 25:
            world.blit(levels_bg_img, backdropbox)
        
            if isPaused == False and isWin == False and isDeath == False:
                pauseButtonIMG()

                #Working Pause button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 50 <= mouse[0] <= 150 and 50 <= mouse[1] <= 90:
                        isPaused = True
            
            #Temporary Win Button
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_8:
                    isWin = True
                elif event.key == pygame.K_9:
                    isDeath = True
            #Pause Screen
            if isPaused:
                pausePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        isPaused = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isPaused = False
            
            #Win Screen
            if isWin:
                winPopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 550 <= mouse[1] <= 590:
                        pygame.quit()
                    if 310 <= mouse[0] <= 510 and 475 <= mouse[1] <= 515:
                        playingLevel = 1
                        isWin = False
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isWin = False

            #Lose Screen
            if isDeath:
                losePopup()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= mouse[0] <= 500 and 475 <= mouse[1] <= 515:
                        pygame.quit()
                    if 300 <= mouse[0] <= 575 and 400 <= mouse[1] <= 440:
                        page = 2
                        isDeath = False
    
    #Draw World
    pygame.display.update()
    pygame.display.flip()
    clock.tick(fps)
