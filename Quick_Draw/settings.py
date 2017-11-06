import pygame#to initialize pygame
class Settings():#to make  settings class
    def __init__(self):#initialize the class
        self.screen_width = 640#set the screen width
        self.screen_height = 480#set the screen height
        self.title_height = 75

        self.bg_color = (0,230,0)#set the bg.color
        self.bg_image = pygame.image.load("22.png")#load the game's background image

        self.intro_image = pygame.image.load("introscreen.jpg")#to load the intro screen's background image
        self.font_size = 115
        self.small_font = 16
        self.exit_font = 22
        self.title_font = 65
        self.buttonx = 150
        self.button2x = 390
        self.buttony = 350
        self.button_width = 120
        self.button_height = 50
        self.fonty = 35
        self.charay = 381
        self.Play1X= 210
        self.Play2X = 420
        self.recty = 132
        self.rectx1 = 81
        self.rectx2 = 526
