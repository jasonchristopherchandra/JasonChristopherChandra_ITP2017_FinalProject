import pygame#import pygame
import sys#import sys
import time#import time
from settings import Settings#import settings class
from protagonist import Protagonist#import protagonist class
from antagonist import Antagonist#import antagonist class
from pygame.locals import *

def message_display(text,screen):
    ai_settings = Settings()#mke a variable to use the settings class

    largeText = pygame.font.Font('freesansbold.ttf',ai_settings.font_size)#font settings
    TextSurf, TextRect = text_objects(text, largeText)#to screeen.rect the text using the font settings
    TextRect.center = ((ai_settings.screen_width/2),(ai_settings.screen_height/2))#the text's position settings

    screen.blit(TextSurf, TextRect)#to blit the text onto the screen
    pygame.display.update()#update the screen so the text appears on screen

    time.sleep(2)# pauses program for 2 seconds

def text_objects(text,font):
    pygame.font.init()#initialize pygame.font
    textSurface = font.render(text,True,(0,0,0))#to render the text using pygame.font
    return textSurface,textSurface.get_rect()# to rect the text

def button(msg,x,y,w,h,ic,ac,screen):#button 1 settings
    ai_settings = Settings()
    mouse = pygame.mouse.get_pos()#to get mouse's position
    click = pygame.mouse.get_pressed()#so the button becomes clickable
    if x+w > mouse[0] > x and y+h > mouse[1] > y:# to add functionality to the button
        pygame.draw.rect(screen,ic,(x,y,w,h))
        if click[0] == 1:
            run_game()
    else:
        pygame.draw.rect(screen,ac,(x,y,w,h))#to change button color when user's mouse hovers it

    smallText = pygame.font.Font("play.otf",ai_settings.small_font)#font settinga
    textSurf, textRect = text_objects(msg, smallText)#to screen.rect the message using  the font settings
    textRect.center = ( (x+(w/2)), (y+(h/2)) )#to set the text's position

    screen.blit(textSurf, textRect)#to blit the text

def button2(msg,x,y,w,h,ic,ac,screen):#button 2 settings
    ai_settings = Settings()
    mouse = pygame.mouse.get_pos()#to get  mouse's position
    click = pygame.mouse.get_pressed()#so we can click the buttons
    if x+w > mouse[0] > x and y+h > mouse[1] > y:#to add function to button (in this case exit)
        pygame.draw.rect(screen,ic,(x,y,w,h))
        if click[0] == 1:
            sys.exit()

    else:
        pygame.draw.rect(screen,ac,(x,y,w,h))#to change button color when the user's mouse hovers it

    smallText = pygame.font.Font("exit.ttf",ai_settings.exit_font)#font settings for text
    textSurf, textRect = text_objects(msg, smallText)#to screen.rect the text using the Font settings
    textRect.center = ( (x+(w/2)), (y+(h/2)) )#the text's position

    screen.blit(textSurf, textRect)#to blit the text


def Intro():
    pygame.init()#to initialize pygame
    pygame.font.init()#to initialize pygame.font for font settings
    intro = True#to create an intro function

    while intro:
        for event in pygame.event.get():#to quit the intro screen
            if event.type == pygame.QUIT:
                sys.exit()
        ai_settings = Settings()#to use settings from the Settings class in the Intro Screen.
        screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))#intro screen's screen setting

        Text = pygame.font.Font('NASHVILL.TTF',ai_settings.title_font)#font settings for Wild West Quick draw
        TextSurf, TextRect = text_objects("Wild West Quick Draw",Text)#the text and the font settings
        TextRect.center = ((ai_settings.screen_width/2),ai_settings.title_height)# to set Quick Draw Wild West position

        screen.blit(ai_settings.intro_image,ai_settings.intro_image.get_rect())#to make intro's bg image
        screen.blit(TextSurf,TextRect)# to blit Wild West Quick Draw

        button("You Ready?",ai_settings.buttonx,ai_settings.buttony,ai_settings.button_width,ai_settings.button_height,(0,230,0),(0,200,0),screen)#to make start button in intro screen
        button2("Too Scared?",ai_settings.button2x,ai_settings.buttony,ai_settings.button_width,ai_settings.button_height,(255,0,0),(200,0,0),screen=screen)#to make exit button in intro screen

        pygame.display.update()#to update the screen


def run_game():
    pygame.init()#initialize pygame

    pygame.mixer.init() #initialize pygame.mixer for music
    pygame.mixer.music.load("Western.mp3")#to load bg music
    pygame.mixer.music.play()#to play bg music

    ai_settings = Settings()#to use settings from the Settings class in run_game
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))#screen size
    pygame.display.set_caption("Quick Draw!!!")#For Caption

    protagonist = Protagonist(screen,[ai_settings.Play1X,ai_settings.charay])#to create antagonist using the Protagonist Class
    antagonist = Antagonist(screen,[ai_settings.Play2X,ai_settings.charay])#to create antagonist using the Antagonist class

    currentsec1 = time.localtime()[-4]#for timer
    winner = None#to create winner variable.
    while True:
        currentsec2 = time.localtime()[-4]#for timer
        for event in pygame.event.get():#so we can quit the game
            if event.type == pygame.QUIT:
                sys.exit()
            if currentsec2 == (currentsec1 + 6):
                if event.type == KEYDOWN:#to decide the winner and load the bullet sound.
                    if event.key == K_s and winner == None:
                        pygame.mixer.music.load("bullet.mp3")
                        pygame.mixer.music.play()

                        time.sleep(2)

                        winner = "player1"

                    if event.key == K_l and winner == None:
                        pygame.mixer.music.load("bullet.mp3")
                        pygame.mixer.music.play()

                        time.sleep(2)

                        winner = "player2"

        screen.blit(ai_settings.bg_image,ai_settings.bg_image.get_rect())#to blit the bg image
        protagonist.blitme()#to blit protagonist
        antagonist.blitme()#to blit antagonist

        currentsec2 = time.localtime()[-4]
        if currentsec2 == (currentsec1 + 2):# to blit Ready...
            Text = pygame.font.Font('NASHVILL.TTF',ai_settings.title_font)
            TextSurf, TextRect = text_objects("Ready...",Text)
            TextRect.center = ((ai_settings.screen_width/2),ai_settings.title_height)

            screen.blit(TextSurf,TextRect)

        if currentsec2 == (currentsec1 + 4):#to blit steady
            Text = pygame.font.Font('NASHVILL.TTF',ai_settings.title_font)
            TextSurf, TextRect = text_objects("Steady...",Text)
            TextRect.center = ((ai_settings.screen_width/2),ai_settings.title_height)

            screen.blit(TextSurf,TextRect)

        if currentsec2 == (currentsec1 + 5):#to blit "FIRE!!!"
            Text = pygame.font.Font('NASHVILL.TTF',ai_settings.title_font)
            TextSurf, TextRect = text_objects("Fire!!!",Text)
            TextRect.center = ((ai_settings.screen_width/2),ai_settings.title_height)

            screen.blit(TextSurf,TextRect)

        if currentsec2 == (currentsec1 + 6):#to blit Player 1's Instruction in the screen.
            Text = pygame.font.Font('NASHVILL.TTF',ai_settings.title_font)
            TextSurf, TextRect = text_objects("Press S",Text)
            TextRect.center = (ai_settings.rectx1,ai_settings.recty)

            screen.blit(TextSurf,TextRect)

        if currentsec2 == (currentsec1 + 6):#to blit Player 2's Instruction to the screen.
            Text = pygame.font.Font('NASHVILL.TTF',ai_settings.title_font)
            TextSurf, TextRect = text_objects("Press L",Text)
            TextRect.center = (ai_settings.rectx2,ai_settings.recty)

            screen.blit(TextSurf,TextRect)

        if winner == "player1":#to blit "Player 1 Wins !!!" in the screen.
            Text = pygame.font.Font('WOODCUT.TTF',ai_settings.fonty)
            TextSurf, TextRect = text_objects("Player 1 Wins !!!",Text)
            TextRect.center = ((ai_settings.screen_width/2),ai_settings.title_height)

            screen.blit(TextSurf,TextRect)

            if currentsec2 == (currentsec1 + 10):
                time.sleep(3)
                Intro()

        if winner == "player2":#to blit "Player 2 Wins!!!" in the screen.
            Text = pygame.font.Font('WOODCUT.TTF',ai_settings.fonty)
            TextSurf, TextRect = text_objects("Player 2 Wins!!!",Text)
            TextRect.center = ((ai_settings.screen_width/2),ai_settings.title_height)

            screen.blit(TextSurf,TextRect)

            if currentsec2 == (currentsec1 + 10):#to re run the intro screen
                time.sleep(3)
                Intro()

        pygame.display.update()#update the screen

Intro()#calling the intro screen
run_game()#to run the game


'''Credits:
-Georgius Kurli
-Ivan Ezechial Suratno
-Python Crash Course
-PythonProgramming.net: Game Development and Creating Buttons
-StackOverflow.com'''
